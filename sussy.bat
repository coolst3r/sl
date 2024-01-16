@echo off

REM Install Python
choco install python -y

REM Clone the Git repository
git clone https://github.com/coolst3r/db1.git

REM Change directory to the cloned repository
cd db1

REM Install required Python packages
pip install pywin32

REM Run the Python script
python lolz.py
