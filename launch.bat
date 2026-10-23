@echo off
REM Batch script to launch Dice Detection GUI on Windows
REM Windows用バッチスクリプト - Dice Detection GUI起動

setlocal enabledelayedexpansion

REM Set title
title Dice Detection System - Xuc Sac Nhan Dien

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ====================================================
    echo ERROR / LOI: Python is not installed!
    echo ERROR / LOI: Python khong duoc cai dat!
    echo ====================================================
    echo.
    echo Please install Python from https://www.python.org/
    echo.
    pause
    exit /b 1
)

REM Display menu
:menu
cls
echo.
echo ====================================================
echo      XUC SAC NHAN DIEN - DICE DETECTION SYSTEM
echo           Dice Detection System v1.0
echo ====================================================
echo.
echo Choose an option / Chon mot tuy chon:
echo.
echo   1. GUI Application / Ung dung Giao dien
echo      (Recommended / Khuyen khich)
echo.
echo   2. Demo Script / Demo
echo      (Quick demonstration)
echo.
echo   3. Test Setup / Kiem tra Cai dat
echo      (Verify installation)
echo.
echo   4. Show Quick Start / Huong dan Nhanh
echo      (Quick start guide)
echo.
echo   5. Open in Jupyter / Mo trong Jupyter
echo      (Interactive notebook)
echo.
echo   6. Exit / Thoat
echo.
echo ====================================================
echo.
set /p choice="Enter your choice / Nhap lua chon (1-6): "

if "%choice%"=="1" goto gui_app
if "%choice%"=="2" goto demo
if "%choice%"=="3" goto test
if "%choice%"=="4" goto quickstart
if "%choice%"=="5" goto jupyter
if "%choice%"=="6" goto exit_app

echo Invalid choice / Lua chon khong hop le
timeout /t 2 /nobreak
goto menu

:gui_app
echo.
echo Starting GUI Application...
echo Dang khoi dong Ung dung Giao dien...
echo.
python gui_app.py
pause
goto menu

:demo
echo.
echo Starting Demo...
echo Dang khoi dong Demo...
echo.
python demo.py --image ./data/sample.jpg
pause
goto menu

:test
echo.
echo Testing Setup...
echo Kiem tra Cai dat...
echo.
python test_setup.py
pause
goto menu

:quickstart
echo.
echo Showing Quick Start Guide...
echo Hien thi Huong dan Nhanh...
echo.
python quickstart.py
pause
goto menu

:jupyter
echo.
echo Launching Jupyter Notebook...
echo Khoi dong Jupyter Notebook...
echo.
jupyter notebook notebook.ipynb
goto menu

:exit_app
echo.
echo Exiting... / Dang thoat...
echo.
timeout /t 2 /nobreak
exit /b 0
