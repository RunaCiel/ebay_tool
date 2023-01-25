import os
import sys
import pandas as pd
from pandas_datareader.data import get_quote_yahoo
import PySide6
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QTableWidgetItem)
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QObject, QMimeData
from PySide6.QtGui import QPicture, QPixmap, QIcon
from mainpage import Ui_Form


EMS_df = pd.read_csv("csv/EMS_charges.csv", encoding="utf_8", index_col=0)
ePacket_df = pd.read_csv("csv/ePacket_charges.csv", encoding="utf_8", index_col=0)


# PySide6のアプリ本体
class MainWindow(QWidget):
    """Pyside6のアプリ本体
    

        Attributes:
            



    """ 


    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("eBay利益計算ツール")

        self.doller_rate = 140
        self.sale_price = 0
        self.purchase_price = 0
        self.weight = 0
        self.category = ""
        #self.label = QLabel("0")
        #self.page1.label11.setText(0)

        # self.ui.graphicsView.clicked.connect(self.usdjpy_rate)
        EMS_model = PandasModel(EMS_df)
        ePacket_model = PandasModel(ePacket_df)
        self.ui.tableView_2.setModel(EMS_model)
        self.ui.tableView_3.setModel(ePacket_model)

        self.set_icon()
        self.ui.pushButton_2.clicked.connect(self.usdjpy_rate_button_pressed)

    def set_icon(self):

        self.koushin_icon = QIcon(r"image/icon_koushin.png")
        self.koushin_icon = self.koushin_icon.pixmap(30, 30)
        self.ui.pushButton_2.setIcon(self.koushin_icon)


    def usdjpy_rate_button_pressed(self):
        """為替レートを取得する。


        Returns:
            numpy.float64 : ドル円の為替レート


        Examples:

            >>> usdjpy()
                140

        """
        
        self.result = get_quote_yahoo('JPY=X')
        self.ary_result = self.result["price"].values
        self.doller_rate = self.ary_result[0]
        self.ui.label_33.setText(str(self.doller_rate))
    

    # def calc_button_pressed(self):


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


    def category_calc(self, category, sale_price):
        """商品カテゴリーごとに変わる落札手数料を計算する。


        Args:
            category (str) : 該当するカテゴリー
            sale_price (int) : 商品の販売価格($)


        Returns:
            int : 販売価格に対する落札手数料($)


        Examples:

            >>> category_calc("本と雑誌", 50)
                7.3


        Note:
            sale_price(販売価格)がborderline_of_priceの値を超えた場合、
            超えた部分のカテゴリー手数料はover_rateの値で計算される。


        """

        if category == "本と雑誌" or "映画&テレビ" or "音楽":
            self.category_fee = 0.146
            self.borderline_of_price = 7500
            self.over_rate = 0.0235
        elif category == "地金":
            self.category_fee = 0.129
            self.borderline_of_price = 7500
            self.over_rate = 0.07
        elif category == "レディースバッグ&ハンドバッグ":
            self.category_fee = 0.15
            self.borderline_of_price = 2000
            self.over_rate = 0.09
        elif category == "ジュエリー&腕時計":
            self.category_fee = 0.15
            self.borderline_of_price = 5000
            self.over_rate = 0.09
        elif category == "腕時計、部品&付属品":
            if sale_price >= 1000:
                self.category_fee = 0.15
                self.borderline_of_price = 0
                self.over_rate = 0
            elif sale_price >= 7500:
                self.category_fee = 0.065
                self.borderline_of_price = 7500
                self.over_rate = 0.03
        elif category == "ギター&ベース":
            self.category_fee = 0.06
            self.borderline_of_price = 7500
            self.over_rate = 0.0235
        elif category == "スポーツシューズ":
            if sale_price >= 150:
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


        if sale_price >= self.borderline_of_price:
            self.auction_fee = sale_price*self.category_fee + (self.borderline_of_price - sale_price)*self.over_rate
        else:
            self.auction_fee = sale_price * self.category_fee

        return self.auction_fee


    def shipping_ser_gen(self, weight, shipping_method_df):
        """入力した重量に当てはまる送料の1次元リストを作成。


        Args:
            weight (int) : ユーザー入力の重量(g)
            shipping_method_df (dataframe) : csvをデータフレームで取り込んだ送料表(円)

        
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

        self.weight_index = shipping_method_df.index

        for index in reversed(self.weight_index):

            if weight >= index:
                self.weight_index = index
                break
            else:
                pass

        self.shipping_series = shipping_method_df.loc[self.weight_index] 
        self.shipping_series = self.conversion_to_doller(self.shipping_series)

        return self.shipping_series


    def profit_calc(self, purchase_price, sale_price, category, weight, shipping_method_df):
        """利益($)を計算する。


        Args:
            purshase_price(int) : 仕入れ値(円)
            sale_price(int) : 販売価格($)
            category(str) : カテゴリー
            weight(int) : ユーザー入力の重量(g)
            shipping_method_df(dataframe) : csvをデータフレームで取り込んだ送料表(円)


        Returns:
            series : 利益の一次元リスト($)


        Examles:

            >>> profit_calc(1000, 50, "本と雑誌", 500, EMS_df)
                第1地帯    22.92
                第2地帯    19.71
                第3地帯    10.78
                第4地帯     5.42
                第5地帯     7.57


        """

        self.exchange_fees = 0.002 * sale_price
        self.international_payment_fee = 0.0135 * sale_price
        self.material_cost = 1.5

        self.purchase_price = self.conversion_to_doller(purchase_price)
        
        self.auction_fee = self.category_calc(category, sale_price)

        self.profit = sale_price - self.purchase_price - self.material_cost - self.auction_fee - self.international_payment_fee - self.exchange_fees
        self.profit = round(self.profit, 2)

        self.shipping_ser = self.shipping_ser_gen(weight, shipping_method_df)
        self.profit_ser = self.profit - self.shipping_ser

        return self.profit_ser


    def profit_rate_calc(self, sale_price, profit):
        """利益率を計算する。


        Args:
            sale_price(int) : 販売価格($)
            profit(ser) : 利益値($)


        Returns:
            series : 利益率を計算する(%)


        Examples:

            >>> profit = profit_calc(1000, 50, "本と雑誌", 500, EMS_df)
                profit_rate_calc(50, profit)

                第1地帯    45.84
                第2地帯    39.42
                第3地帯    21.56
                第4地帯    10.84
                第5地帯    15.14
        

        """

        self.profit_rate = profit / sale_price * 100
        return self.profit_rate


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