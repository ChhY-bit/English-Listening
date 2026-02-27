@echo off
chcp 65001 > nul
python "%~dp0create_daily_note.py"
pause
