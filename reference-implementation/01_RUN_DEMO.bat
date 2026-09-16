@echo off
setlocal
cd /d "%~dp0"
title M-PIN Reference Implementation v0.1b Verified - Demo

echo ================================================
echo   M-PIN Reference Implementation v0.1b Verified

echo   Demo: Connect - Load - Save/No Save - Commit

echo ================================================
echo.

where py >nul 2>nul
if %errorlevel%==0 (
  py -3 demo.py
) else (
  where python >nul 2>nul
  if %errorlevel%==0 (
    python demo.py
  ) else (
    echo [ERROR] Python was not found.
    echo Install Python 3.11 or later, then run this file again.
  )
)

echo.
echo ================================================
echo   Finished. Press any key to close this window.
echo ================================================
pause >nul
endlocal
