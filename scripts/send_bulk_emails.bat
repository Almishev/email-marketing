@echo off
chcp 65001 > nul
echo Масово изпращане на имейли
echo.
echo Ще бъдат използвани имейлите от файла email_list.txt
echo.
set /p "subject=Въведете тема на имейла (натиснете Enter за 'Специални предложения от semma.bg'): "

if "%subject%"=="" set subject=Специални предложения от semma.bg

echo.
echo Изпращане на имейли с тема "%subject%"...
python "%~dp0send_email.py" --file "%~dp0email_list.txt" --subject "%subject%"

echo.
echo Натиснете произволен клавиш, за да затворите прозореца...
pause > nul