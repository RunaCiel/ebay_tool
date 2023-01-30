import os
import sys
import pandas as pd
from pandas_datareader.data import get_quote_yahoo
import PySide6
from PySide6.QtWidgets import (QApplication, QWidget, QItemDelegate)
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QIcon, QColor
from mainpage import Ui_Form

# PySide6のアプリ本体
class MainWindow(QWidget):
    """Pyside6のアプリ本体


    """ 


    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("eBay利益計算ツール")

        self.EMS_df = pd.read_csv("csv/EMS_charges.csv", encoding="utf_8", index_col=0)
        self.ePacket_df = pd.read_csv("csv/ePacket_charges.csv", encoding="utf_8", index_col=0)

        EMS_model = PandasModel(self.EMS_df)
        ePacket_model = PandasModel(self.ePacket_df)
        self.ui.tableView_2.setModel(EMS_model)
        self.ui.tableView_3.setModel(ePacket_model)

        self.set_picture()
        self.set_connect()


    def set_picture(self):
        """画像をセットする。
        
        """

        self.koushin_icon = QIcon(r"image/icon_koushin.png")
        self.koushin_icon = self.koushin_icon.pixmap(30, 30)
        self.ui.pushButton_2.setIcon(self.koushin_icon)


    def set_connect(self):
        """シグナルとスロットの紐づけ。
        
        """

        self.ui.pushButton_2.clicked.connect(self.usdjpy_rate_button_pressed)
        self.ui.pushButton.clicked.connect(self.calc_button_pressed)
        self.ui.buttonGroup.buttonClicked.connect(self.radiobutton_checked)


    def usdjpy_rate_button_pressed(self):
        """為替レートを取得する。


        """
        
        self.result = get_quote_yahoo('JPY=X')
        self.ary_result = self.result["price"].values
        self.doller_rate = self.ary_result[0]
        self.ui.label_33.setText(str(self.doller_rate))


    def calc_button_pressed(self):
        """「計算」ボタンを押したときの処理。
        

        Note:
            purshase_price : 仕入れ値(円)
            sale_price : 販売価格($)
            category : カテゴリー
            weight : ユーザー入力の重量(g)

        """

        try:
            self.doller_rate
            
        except AttributeError:
            self.ui.label.setText("為替レートを更新してください")

        else:
            self.ui.label.setText("")
            try:
                self.sale_price = int(self.ui.lineEdit_8.text())
            except ValueError:
                self.ui.label.setText("販売価格を入力してください")
            else:
                self.ui.label.setText("")

                try:
                    self.purchase_price = int(self.ui.lineEdit_9.text())
                except ValueError:
                    self.purchase_price = 0

                try:
                    self.weight = int(self.ui.lineEdit_7.text())
                except ValueError:
                    self.weight = 500

                self.category = self.ui.comboBox_3.currentText()

                EMS_model = self.dataframe_gen(self.EMS_df)
                EMS_model = PandasModel(EMS_model)
                self.ui.tableView_2.setModel(EMS_model)
                ePacket_model = self.dataframe_gen(self.ePacket_df)
                ePacket_model = PandasModel(ePacket_model)
                self.ui.tableView_3.setModel(ePacket_model)
                self.radiobutton_checked()


    def radiobutton_checked(self):
        """「表示」ラジオボタンの処理。
        
        """

        self.ui.buttonGroup.setId(self.ui.radioButton_5, 1)
        self.ui.buttonGroup.setId(self.ui.radioButton_6, 2)
        # 詳細
        if self.ui.buttonGroup.checkedId() == 2:
            self.ui.tableView_2.showColumn(5)
            self.ui.tableView_2.showColumn(6)
            self.ui.tableView_2.showColumn(7)
            self.ui.tableView_2.showColumn(8)
            self.ui.tableView_3.showColumn(5)
            self.ui.tableView_3.showColumn(6)
            self.ui.tableView_3.showColumn(7)
            self.ui.tableView_3.showColumn(8)
            
        # デフォルト
        elif self.ui.buttonGroup.checkedId() == 1:
            self.ui.tableView_2.setColumnHidden(5, True)
            self.ui.tableView_2.setColumnHidden(6, True)
            self.ui.tableView_2.setColumnHidden(7, True)
            self.ui.tableView_2.setColumnHidden(8, True)
            self.ui.tableView_3.setColumnHidden(5, True)
            self.ui.tableView_3.setColumnHidden(6, True)
            self.ui.tableView_3.setColumnHidden(7, True)
            self.ui.tableView_3.setColumnHidden(8, True)


    def dataframe_gen(self, shipping_method_df):
        """TableViewに表示させるデータフレームの作成。
        

        Args:
            shipping_method_df(DataFrame) : 送料表
        

        Returns:
            DataFrame : 円から変換したドルの値


        """

        self.shipping_method_df = shipping_method_df
        self.category_calc()
        self.profit_ser = self.profit_calc()
        self.profit_df = pd.DataFrame(self.profit_ser)
        self.profit_rate_list = self.profit_rate_calc()
        self.profit_df["利益率"] = self.profit_rate_list
        self.profit_df = self.profit_df.rename(columns={self.weight: "利益($)"})
        self.profit_df["販売価格($)"] = self.sale_price

        self.shipping_series = self.shipping_ser_gen()

        self.profit_df["仕入れ値($)"] = self.purchase_price
        self.profit_df["送料($)"] = self.shipping_series
        self.profit_df["落札手数料($)"] = self.auction_fee
        self.profit_df["国際決済手数料($)"] = self.international_payment_fee
        self.profit_df["梱包費($)"] = self.material_cost
        self.profit_df["為替手数料($)"] = self.exchange_fees

        return self.profit_df


    def conversion_to_doller(self, jpy):
        """日本円をドルに変換する。


        Args:
            jpy(float) : 円の値
        

        Returns:
            float : 円から変換したドルの値
        

        Examples:

            >>> doller_rate = 140
                conversion_to_doller(5000)
                35.71


        """

        self.doller = jpy / self.doller_rate
        self.doller = round(self.doller, 2)

        return self.doller
    

    def conversion_to_jpy(self, doller):
        """ドルを日本円に変換する。


        Args:
            doller(float) : ドルの値
        

        Returns:
            float : ドルから変換した円の値
        

        Examples:

            >>> doller_rate = 140
                conversion_to_jpy(50.55)
                7077.0


        """

        self.jpy = doller * self.doller_rate

        return self.jpy


    def category_calc(self):
        """商品カテゴリーごとに変わる落札手数料を計算する。


        Returns:
            int : 販売価格に対する落札手数料($)


        Examples:

            >>> category_calc("本と雑誌", 50)
                7.3


        Note:
            sale_price(販売価格)がborderline_of_priceの値を超えた場合、
            超えた部分のカテゴリー手数料はover_rateの値で計算される。


        """

        if self.category == "本と雑誌" or self.category == "映画&テレビ" or self.category == "音楽":
            self.category_fee = 0.146
            self.borderline_of_price = 7500
            self.over_rate = 0.0235
        elif self.category == "地金":
            self.category_fee = 0.129
            self.borderline_of_price = 7500
            self.over_rate = 0.07
        elif self.category == "レディースバッグ&ハンドバッグ":
            self.category_fee = 0.15
            self.borderline_of_price = 2000
            self.over_rate = 0.09
        elif self.category == "ジュエリー&腕時計":
            self.category_fee = 0.15
            self.borderline_of_price = 5000
            self.over_rate = 0.09
        elif self.category == "腕時計、部品&付属品":
            if self.sale_price >= 1000:
                self.category_fee = 0.15
                self.borderline_of_price = 0
                self.over_rate = 0
            elif self.sale_price >= 7500:
                self.category_fee = 0.065
                self.borderline_of_price = 7500
                self.over_rate = 0.03
        elif self.category == "ギター&ベース":
            self.category_fee = 0.06
            self.borderline_of_price = 7500
            self.over_rate = 0.0235
        elif self.category == "スポーツシューズ":
            if self.sale_price >= 150:
                self.category_fee = 0.08
                self.borderline_of_price = 0
                self.over_rate = 0
            else:
                self.category_fee = 0.129
                self.borderline_of_price = 0
                self.over_rate = 0
        else:
            self.category_fee = 0.129
            self.borderline_of_price = 7500
            self.over_rate = 0.0235


        if self.sale_price >= self.borderline_of_price:
            self.auction_fee = self.sale_price*self.category_fee + (self.borderline_of_price - self.sale_price)*self.over_rate
        else:
            self.auction_fee = self.sale_price * self.category_fee

        return self.auction_fee


    def shipping_ser_gen(self):
        """入力した重量に当てはまる送料の1次元リストを作成。

        
        Returns:
            series : 送料表から重量に当てはまる送料行を抜き出した1次元リスト

        
        Examples:

            >>> shipping_ser_gen(500, EMS_df)
                第1地帯    10.36
                第2地帯    13.57
                第3地帯    22.50
                第4地帯    27.86
                第5地帯    25.71


        """

        self.weight_index = self.shipping_method_df.index

        for index in reversed(self.weight_index):

            if self.weight >= index:
                self.weight_index = index
                break
            else:
                pass

        self.shipping_series = self.shipping_method_df.loc[self.weight_index] 
        self.shipping_series = self.conversion_to_doller(self.shipping_series)

        return self.shipping_series


    def profit_calc(self):
        """利益($)を計算する。


        Returns:
            series : 地域ごとの利益の一次元リスト($)


        """

        self.purchase_price = self.conversion_to_doller(self.purchase_price)

        self.exchange_fees = 0.002 * self.sale_price
        self.international_payment_fee = 0.0135 * self.sale_price
        self.material_cost = 1.5

        self.profit = self.sale_price - self.purchase_price - self.material_cost - self.auction_fee - self.international_payment_fee - self.exchange_fees
        self.profit = round(self.profit, 2)

        self.shipping_ser = self.shipping_ser_gen()
        self.profit_ser = self.profit - self.shipping_ser
        self.profit_ser = round(self.profit_ser, 2)

        return self.profit_ser


    def profit_rate_calc(self):
        """利益率を計算する。


        Returns:
            series : 地域ごとの利益率(%)の一次元リスト


        """

        self.profit_rate = self.profit_ser / self.sale_price * 100
        self.list = list(self.profit_rate)
        self.profit_rate_list = []
        for i in self.list:
            i = round(i)
            i = str(i) + "%"
            self.profit_rate_list.append(i)
        return self.profit_rate_list


class PandasModel(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe """

    def __init__(self, dataframe: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe

    def rowCount(self, parent=QModelIndex()) -> int:
        """ Override method from QAbstractTableModel

        Return row count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return column count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe.columns)
        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return data cell from the pandas DataFrame
        """
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return str(self._dataframe.iloc[index.row(), index.column()])

        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as horizontal header data.
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._dataframe.columns[section])

            if orientation == Qt.Vertical:
                return str(self._dataframe.index[section])

        return None



if __name__ == "__main__":

    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    
    app = QApplication(sys.argv)  
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())