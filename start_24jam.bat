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
set EXITCODE=%errorlevel%

if %EXITCODE% equ 99 (
    echo.
    echo [INFO] Watchdog sudah berjalan di proses lain. Jendela ini akan ditutup otomatis...
    timeout /t 5 /nobreak >nul
    exit /b
)

echo.
echo [WARNING] Watchdog berhenti/crash tak terduga! (Exit Code: %EXITCODE%)
echo Menunggu 5 detik sebelum auto-restart...
timeout /t 5 /nobreak >nul
goto loop

