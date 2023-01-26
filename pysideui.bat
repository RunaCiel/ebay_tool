@echo off
@setlocal enabledelayedexpansion

REM ドラッグ＆ドロップされたファイルをforでまわす
for %%A in (%*) do (
    REM 拡張子が.uiだったら処理続行
    if "%%~xA"==".ui" (
        REM 変数OutputFileにアウトプットしたいフルパスをセットする
        REM %%~dA = ドライブ名, %%~pA = パス, %%~nA = ファイル名
        set OutputFile="%%~dA%%~pA%%~nA.py"
        REM %hoge%とすると中身がなくなるので遅延環境変数 !hoge! を使う
        echo Convert to !OutputFile!
        C:\Users\runa1\Documents\eBayTool\eBayTool\Scripts\pyside6-uic.exe %%A -o !OutputFile!
    )
)
pause