@echo off
chcp 65001 > nul
echo Изпращане на единичен имейл
set /p recipient="Въведете имейл адрес на получателя: "
set /p "subject=Въведете тема на имейла (натиснете Enter за 'Специални предложения от semma.bg'): "

if "%subject%"=="" set subject=Специални предложения от semma.bg

echo.
echo Изпращане на имейл до %recipient% с тема "%subject%"...
python "%~dp0send_email.py" --recipient "%recipient%" --subject "%subject%"

echo.
echo Натиснете произволен клавиш, за да затворите прозореца...
pause > nul