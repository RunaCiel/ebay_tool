import pandas as pd
import PySide6
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QRadioButton, QLineEdit)

import os
import sys

# 為替レートの取得
doller = 140

# 利益計算
class ProfitCalc:
    # カテゴリー選択時の落札手数料算出

    EMS_df = pd.read_csv("csv/EMS_charges.csv", index_col=0)
    ePacket_df = pd.read_csv("csv/ePacket_charges.csv", index_col=0)

    profit = 0             # 利益
    final_value_fee = 0    # 落札手数料
    international_fee = 0.0135  # 海外決済手数料
    exchange_fees = 0.002  # 為替手数料
    material_cost = 150    # 梱包材料費
    shipping_fee = 0       # 送料

    # ユーザー入力
    purchase_price = 0  # 仕入れ価格
    sale_price = 0      # 販売価格(送料含む)
    profit_ratio = 0    # 利益率
    category = 0        # カテゴリー
    weight = 0          # 重量

    def category_calc(self, category, sale_price):
        category_fee = 0
        over_price = 0  # 手数料が変わる販売総額のボーダーライン
        over_rate = 0   # ボーダーラインを超えた部分に対する手数料
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

        return category_fee, over_price, over_rate

# PySide6のアプリ本体
class MainWindow(QWidget):              
    def __init__(self, parent=None):    
        super().__init__(parent)        

        # ウィンドウタイトル
        self.setWindowTitle("eBay利益計算ツール")

        # ウィンドウサイズ
        windowWidth = 1000
        windowHeight = 800
        self.resize(windowWidth, windowHeight)

        self.SetButton()
        # self.SetRadio()
        # self.SetLabel()
        
    # ボタンのメソッド
    def SetButton(self):
        button = QPushButton(self)


if __name__ == "__main__":
    # 環境変数にPySide6を登録
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    
    app = QApplication(sys.argv)    # PySide6の実行
    window = MainWindow()           # ユーザがコーディングしたクラス
    window.show()                   # PySide6のウィンドウを表示
    sys.exit(app.exec())            # PySide6の終了