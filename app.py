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