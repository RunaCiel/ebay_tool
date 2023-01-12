import pandas as pd
from pandas_datareader.data import get_quote_yahoo
import PySide6
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QRadioButton, QLineEdit)

import os
import sys

EMS_df = pd.read_csv("csv/EMS_charges.csv", encoding="utf_8", index_col=0)          # EMSのcsvをデータフレームとして取り込み
ePacket_df = pd.read_csv("csv/ePacket_charges.csv", encoding="utf_8", index_col=0)  # epacketのcsvをデータフレームとして取り込み

# ユーザー入力
purchase_price = 0  # 仕入れ価格(円)
sale_price = 0      # 販売価格(送料含む)($)

# 為替レートの取得
def usdjpy():
    result = get_quote_yahoo('JPY=X')
    ary_result = result["price"].values
    doller_rate = ary_result[0]

    return doller_rate

# 落札手数料算出
def category_calc(category, sale_price):

    category_fee = 0  # 落札手数料(%)
    over_price = 0    # 手数料が変わる販売総額のボーダーライン($)
    over_rate = 0     # ボーダーラインを超えた部分に対する手数料(%)
    # カテゴリーごとの落札手数料を検索
    if category == "本と雑誌" or "映画&テレビ" or "音楽":
        category_fee = 0.146
        over_price = 7500
        over_rate = 0.0235
    elif category == "地金":
        category_fee = 0.129
        over_price = 7500
        over_rate = 0.07
    elif category == "レディースバッグ&ハンドバッグ":
        category_fee = 0.15
        over_price = 2000
        over_rate = 0.09
    elif category == "ジュエリー&腕時計":
        category_fee = 0.15
        over_price = 5000
        over_rate = 0.09
    elif category == "腕時計、部品&付属品":
        if sale_price >= 1000:
            category_fee = 0.15
            over_price = 0
            over_rate = 0
        elif sale_price >= 7500:
            category_fee = 0.065
            over_price = 7500
            over_rate = 0.03
    elif category == "ギター&ベース":
        category_fee = 0.06
        over_price = 7500
        over_rate = 0.0235
    elif category == "スポーツシューズ":
        if sale_price >= 150:
            category_fee = 0.08
            over_price = 0
            over_rate = 0
        else:
            category_fee = 0.129
            over_price = 0
            over_rate = 0
    else:
        category_fee = 0.129
        over_price = 7500
        over_rate = 0.0235

    # 手数料計算($)
    if sale_price >= over_price:
        final_value_fee = sale_price * category_fee + (over_price - sale_price) * over_rate
    else:
        final_value_fee = sale_price * category_fee

    return final_value_fee

# 重量表作成（$）
def weight_df(weight, df):
    # index取り出し
    weight_index = df.index

    for index in reversed(weight_index):
        # 重量が当てはまるインデックスを検出
        if weight >= index:
            weight_index = index  # 検出したら代入し、ループを抜ける
            break
        else:
            pass

    new_df = df.loc[weight_index]  # 重量から対象行を取り出し
    new_df = new_df / doller_rate   # ドルに変換
    new_df = round(new_df, 2)  # 小数点以下2桁に四捨五入

    return new_df

# 地域ごとの利益算出($)
def profit_calc(purchase_price, sale_price, category, weight, df):
    exchange_fees = 0.002 * sale_price      # 為替手数料($)
    international_fee = 0.0135 * sale_price  # 海外決済手数料($)
    material_cost = 1.5         # 梱包材料費($)

    purchase_price = conversion_to_doller(purchase_price)  # 仕入れ価格をドルに変換
    
    final_value_fee = category_calc(category, sale_price)  # 落札手数料

    profit = sale_price - purchase_price - material_cost - final_value_fee - international_fee - exchange_fees
    profit = round(profit, 2)  # 送料をまだ引いていない利益額($)

    shipping_df = weight_df(weight, df)  # 入力した重量の送料表を、抜き出して代入
    profit_df = profit - shipping_df     # 送料を引いた最終的な利益表($)

    return profit_df

# 利益率の計算(%)、引数はドルで入力
def profit_ratio_calc(sale_price, profit):
    profit_ratio = profit / sale_price * 100  # 利益率(%)
    return profit_ratio

# 日本円に変換
def conversion_to_jpy(doller):
    jpy = doller * doller_rate

    return jpy

# ドルに変換
def conversion_to_doller(jpy):
    doller = jpy / doller_rate

    return doller