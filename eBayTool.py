import pandas as pd
from pandas_datareader.data import get_quote_yahoo
import PySide6
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QRadioButton, QLineEdit)

import os
import sys

EMS_df = pd.read_csv("csv/EMS_charges.csv", encoding="utf_8", index_col=0)
ePacket_df = pd.read_csv("csv/ePacket_charges.csv", encoding="utf_8", index_col=0)

# ユーザー入力
purchase_price = 0
sale_price = 0

def usdjpy_rate():
    """為替レートを取得する。


    Returns:
        numpy.float64 : ドル円の為替レート


    Examples:

        >>> usdjpy()
            140

    """
    result = get_quote_yahoo('JPY=X')
    ary_result = result["price"].values
    doller_rate = ary_result[0]

    return doller_rate


def category_calc(category, sale_price):
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
        category_fee = 0.146
        borderline_of_price = 7500
        over_rate = 0.0235
    elif category == "地金":
        category_fee = 0.129
        borderline_of_price = 7500
        over_rate = 0.07
    elif category == "レディースバッグ&ハンドバッグ":
        category_fee = 0.15
        borderline_of_price = 2000
        over_rate = 0.09
    elif category == "ジュエリー&腕時計":
        category_fee = 0.15
        borderline_of_price = 5000
        over_rate = 0.09
    elif category == "腕時計、部品&付属品":
        if sale_price >= 1000:
            category_fee = 0.15
            borderline_of_price = 0
            over_rate = 0
        elif sale_price >= 7500:
            category_fee = 0.065
            borderline_of_price = 7500
            over_rate = 0.03
    elif category == "ギター&ベース":
        category_fee = 0.06
        borderline_of_price = 7500
        over_rate = 0.0235
    elif category == "スポーツシューズ":
        if sale_price >= 150:
            category_fee = 0.08
            borderline_of_price = 0
            over_rate = 0
        else:
            category_fee = 0.129
            borderline_of_price = 0
            over_rate = 0
    else:
        category_fee = 0.129
        borderline_of_price = 7500
        over_rate = 0.0235


    if sale_price >= borderline_of_price:
        auction_fee = sale_price*category_fee + (borderline_of_price - sale_price)*over_rate
    else:
        auction_fee = sale_price * category_fee

    return auction_fee


def shipping_ser_gen(weight, shipping_method_df):
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

    weight_index = shipping_method_df.index

    for index in reversed(weight_index):

        if weight >= index:
            weight_index = index
            break
        else:
            pass

    shipping_series = shipping_method_df.loc[weight_index] 
    shipping_series = conversion_to_doller(shipping_series)

    return shipping_series


def profit_calc(purchase_price, sale_price, category, weight, shipping_method_df):
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

    exchange_fees = 0.002 * sale_price
    international_payment_fee = 0.0135 * sale_price
    material_cost = 1.5

    purchase_price = conversion_to_doller(purchase_price)
    
    auction_fee = category_calc(category, sale_price)

    profit = sale_price - purchase_price - material_cost - auction_fee - international_payment_fee - exchange_fees
    profit = round(profit, 2)

    shipping_ser = shipping_ser_gen(weight, shipping_method_df)
    profit_ser = profit - shipping_ser

    return profit_ser


def profit_rate_calc(sale_price, profit):
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

    profit_rate = profit / sale_price * 100
    return profit_rate


def conversion_to_jpy(doller):
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

    jpy = doller * doller_rate

    return jpy


def conversion_to_doller(jpy):
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

    doller = jpy / doller_rate
    doller = round(doller, 2)

    return doller


doller_rate = 140


# PySide6のアプリ本体
class MainWindow(QWidget):
    """Pyside6のアプリ本体
    

        Attributes:
            setWindowTitle(str) : ウィンドウタイトル
            resize : ウィンドウサイズ



    """ 


    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("eBay利益計算ツール")

        # windowWidth = 1000
        # windowHeight = 800
        # self.resize(windowWidth, windowHeight)

        # self.SetButton()
        # self.SetRadio()
        # self.SetLabel()
        
        
    # def SetButton(self):
    #     button = QPushButton(self)


if __name__ == "__main__":

    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    
    app = QApplication(sys.argv)

    ui_file = Qfile("page1.ui")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())