@echo off
cd %~dp0
if exist .venv\\Scripts\\activate.bat (
    call .venv\\Scripts\\activate.bat
)
python tool.py