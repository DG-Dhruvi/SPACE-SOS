@echo off
title Space Station Object Detection System
color 0B

echo.
echo     =========================================
echo     SPACE STATION DETECTION SYSTEM
echo     =========================================
echo.
echo     Initializing system...
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    echo    Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

if not exist "app_launcher.py" (
    echo app_launcher.py not found in current directory
    pause
    exit /b 1
)

echo     Starting application launcher...
.\venv_new\Scripts\python.exe app_launcher.py

if errorlevel 1 (
    echo.
    echo Application failed to start
    pause
) else (
    echo.
    echo Application closed successfully
)

pause
exit /b 0