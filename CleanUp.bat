@echo off
chcp 65001 >nul
set title_script=Folder Cleanup Script
title %title_script%
set ansi_code_page=1252
REM Created by Ahmed Sagarwala on 2024-06-10
setlocal enabledelayedexpansion
cls

echo --------------=======================-----------------
echo              Cleanup Time: %time%
echo --------------=======================-----------------
echo ██╗  ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗     ██████╗  ██████╗ ██████╗  ██████╗ 
echo ██║  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ╚════██╗██╔═████╗╚════██╗██╔════╝ 
echo ███████║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝     █████╔╝██║██╔██║ █████╔╝███████╗ 
echo ██╔══██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██╔═══╝ ████╔╝██║██╔═══╝ ██╔═══██╗
echo ██║  ██║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ███████╗╚██████╔╝███████╗╚██████╔╝
echo ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ 
echo --------------=======================-----------------
echo This script will clean up the SCAN and OUTPUT folders.
cd /d "C:\Users\Ahmed\Documents\ComfyUI\input\scan"
if exist *.png (
    move *.png .\autoshow
) else (
    echo SCAN Folder: No PNG files found
)

cd /d "C:\Users\Ahmed\Documents\ComfyUI\output"
if exist *.png (
    move *.png .\printed
) else (
    echo OUTPUT Folder: No PNG files found
)

timeout /t 2 /nobreak >nul
