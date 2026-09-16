@echo off
setlocal
cd /d "%~dp0"
title M-PIN Reference Implementation v0.1b Verified - Tests

echo ================================================
echo   M-PIN v0.1b Verified Conformance Tests

echo ================================================
echo.

where py >nul 2>nul
if %errorlevel%==0 (
  py -3 -m unittest discover -s tests -v
) else (
  where python >nul 2>nul
  if %errorlevel%==0 (
    python -m unittest discover -s tests -v
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
