@echo off
setlocal

rem Define environment variables
set SDK_PATH=tiktok-business-api-sdk
set MYVEVN=venv_ttcm
set PYTHONPATH=%SDK_PATH%;%SDK_PATH%\python_sdk;%SDK_PATH%\python_sdk\business_api_client

rem Save the current directory
set "CURRENT_DIR=%CD%"

rem Check if the virtual environment already exists
if not exist "%MYVEVN%" (
    echo =======================================================
    echo Creating virtual environment...
    python3 -m venv %MYVEVN%
    echo =======================================================
    echo Virtual environment created.
    echo =======================================================
    echo Activating virtual environment...
    call %MYVEVN%\Scripts\activate
    echo =======================================================
    echo Virtual environment activated.
) else (
    echo =======================================================
    echo Virtual environment %MYVEVN% already exists. Skipping creation.
    echo =======================================================
)

rem Navigate to the SDK folder
echo =======================================================
echo Navigating to SDK folder...
cd %SDK_PATH%\python_sdk
echo =======================================================
echo SDK folder navigation complete.

rem Install dependencies and Python package
echo =======================================================
echo Installing dependencies...
pip install -r requirements.txt
echo =======================================================
echo Dependencies installed.

echo =======================================================
echo Installing Python package...
python setup.py install
echo =======================================================
echo Python package installed.

rem Return to the original directory
echo =======================================================
echo Returning to original directory...
cd /d "%CURRENT_DIR%"
echo =======================================================
echo Original directory navigation complete.

endlocal
