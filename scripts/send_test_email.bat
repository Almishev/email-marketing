@echo off
chcp 65001 > nul
echo Изпращане на тестов имейл
set /p recipient="Въведете имейл адрес за тестване: "

echo.
echo Изпращане на тестов имейл до %recipient%...
python "%~dp0send_email.py" --recipient "%recipient%" --subject "Тестов имейл от semma.bg"

echo.
echo Натиснете произволен клавиш, за да затворите прозореца...
pause > nul