@echo off
title OTP IVA SMS - 24/7 Watchdog Supervisor
color 0A

echo =======================================================
echo   OTP IVA SMS - 24/7 AUTO RECOVERY & SUPERVISOR
echo =======================================================
echo.

cd /d "%~dp0"

:loop
echo [%date% %time%] Memulai Watchdog 24/7...
python watchdog.py

echo.
echo [WARNING] Watchdog berhenti/crash tak terduga!
echo Menunggu 5 detik sebelum auto-restart...
timeout /t 5 /nobreak >nul
goto loop
