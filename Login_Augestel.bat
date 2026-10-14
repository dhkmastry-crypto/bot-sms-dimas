@echo off
chcp 65001 >nul
color 0B
title Augestel Login Helper (Akun 10 - 16)

:MENU
cls
echo ======================================================================
echo          🌐 AUGESTEL 1-TIME BROWSER LOGIN HELPER (AKUN 10 - 16)
echo ======================================================================
echo  Akun Augestel hanya butuh login 1 KALI dengan 'Remember me'.
echo  Setelah itu cookie sesi aktif tersimpan permanen di RAM 24/7!
echo.
echo  Daftar Akun yang Belum Login:
echo   [10] keztokitems@gmail.com       (Password: dimas098.)
echo   [11] dimasganteung69@gmail.com   (Password: dimas098.)
echo   [12] maskupukupu15@gmail.com     (Password: dimas098.)
echo   [13] songkanjut@gmail.com        (Password: dimas098.)
echo   [14] dimsongkang@gmail.com       (Password: dimas098.)
echo   [15] dimaseu542@gmail.com        (Password: dimas098.)
echo   [16] mulyanasurin@gmail.com      (Password: dimas098.)
echo.
echo   [X] Keluar
echo ======================================================================
set /p CHOICE="Pilih nomor akun yang ingin dibuka (10-16): "

if /i "%CHOICE%"=="X" goto END
if %CHOICE% GEQ 10 if %CHOICE% LEQ 16 goto PROCESS_LOGIN

echo Pilihan tidak valid! Masukkan angka antara 10 sampai 16.
timeout /t 2 /nobreak >nul
goto MENU

:PROCESS_LOGIN
set ACC=%CHOICE%
set EMAIL=
if "%ACC%"=="10" set EMAIL=keztokitems@gmail.com
if "%ACC%"=="11" set EMAIL=dimasganteung69@gmail.com
if "%ACC%"=="12" set EMAIL=maskupukupu15@gmail.com
if "%ACC%"=="13" set EMAIL=songkanjut@gmail.com
if "%ACC%"=="14" set EMAIL=dimsongkang@gmail.com
if "%ACC%"=="15" set EMAIL=dimaseu542@gmail.com
if "%ACC%"=="16" set EMAIL=mulyanasurin@gmail.com

cls
echo ======================================================================
echo   MEMPROSES LOGIN UNTUK AKUN #%ACC% (%EMAIL%)
echo ======================================================================
echo.
echo [1/3] Menutup profil background di RAM agar tidak bentrok (lock file)...
curl -s -X POST http://localhost:5000/api/augestel/pool/close-context/%ACC% -H "X-Internal-Token: bot-internal-secret" >nul 2>&1
timeout /t 1 /nobreak >nul

del /f /q "C:\Users\ADMIN\Downloads\OTP IVA SMS\browser_profile_augestel_%ACC%\lockfile" >nul 2>&1
del /f /q "C:\Users\ADMIN\Downloads\OTP IVA SMS\browser_profile_augestel_%ACC%\SingletonLock" >nul 2>&1
del /f /q "C:\Users\ADMIN\Downloads\OTP IVA SMS\browser_profile_augestel_%ACC%\SingletonSocket" >nul 2>&1
del /f /q "C:\Users\ADMIN\Downloads\OTP IVA SMS\browser_profile_augestel_%ACC%\SingletonCookie" >nul 2>&1

echo.
echo [2/3] Membuka Microsoft Edge asli di layar desktop Anda sekarang...
echo.
echo  ------------------------------------------------------------------
echo   📋 KREDENSIAL UNTUK DIISI DI HALAMAN LOGIN:
echo   - Email    : %EMAIL%
echo   - Password : dimas098.
echo   - CENTANG  : [x] Remember me   <-- PENTING AGAR SESI TIDAK EXPIRED!
echo   - Quick Check: Hubungkan benang puzzle (3 detik), lalu klik Sign In!
echo  ------------------------------------------------------------------
echo.
start "" "msedge.exe" --user-data-dir="C:\Users\ADMIN\Downloads\OTP IVA SMS\browser_profile_augestel_%ACC%" "https://augestel.com/Switchfy"

echo Setelah Anda berhasil login dan melihat portal Augestel:
echo TUTUP jendela Microsoft Edge tersebut, lalu kembali ke sini...
echo.
pause

echo.
echo [3/3] Memuat kembali Akun #%ACC% ke Memory Pool RAM 24/7...
curl -s -X POST http://localhost:5000/api/augestel/pool/reinit/%ACC% -H "X-Internal-Token: bot-internal-secret"
echo.
echo ======================================================================
echo  🎉 SELESAI! Akun #%ACC% (%EMAIL%) sekarang sudah standby di RAM!
echo ======================================================================
echo.
set /p AGAIN="Ingin login akun berikutnya? (Y/N): "
if /i "%AGAIN%"=="Y" goto MENU

:END
echo Menutup...
timeout /t 1 /nobreak >nul
exit
