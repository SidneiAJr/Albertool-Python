@echo off
echo ====================================
echo   BUILD - Gerando .exe com PyInstaller
echo ====================================

:: ===== CONFIGURAÇÕES =====
set NOME=MeuApp
set ARQUIVO=main.py
set ICONE=icon.ico

:: ===== BUILD SIMPLES (sem icone) =====
:: pyinstaller --onefile --windowed --name=%NOME% %ARQUIVO%

:: ===== BUILD COMPLETO (com icone) =====
pyinstaller --onefile --windowed --name=%NOME% --icon=%ICONE% %ARQUIVO%

echo.
echo ✅ Build finalizado!
echo 📁 Executável gerado em: dist/%NOME%.exe
pause
