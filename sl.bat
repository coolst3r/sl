@echo off

REM Install Python
choco install python -y

REM Clone the Git repository
git clone <repository_url>

REM Change directory to the cloned repository
cd <repository_name>

REM Install required Python packages
pip install -r requirements.txt

REM Run the Python script
python <script_name>.py
