@echo off
setlocal
cd /d "%~dp0"

if not exist output mkdir output

xelatex -interaction=nonstopmode -halt-on-error -output-directory=output main.tex
if errorlevel 1 goto failed

xelatex -interaction=nonstopmode -halt-on-error -output-directory=output main.tex
if errorlevel 1 goto failed

copy /Y "output\main.pdf" "output\Progress_AuditChain_Gateway_September_2026_Lengkap_Update.pdf" >nul
echo.
echo Build selesai:
echo output\Progress_AuditChain_Gateway_September_2026_Lengkap_Update.pdf
exit /b 0

:failed
echo.
echo Build gagal. Cek file output\main.log
exit /b 1
