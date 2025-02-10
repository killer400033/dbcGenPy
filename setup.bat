@echo off
setlocal

:: Define the Python download URL and target file
set PYTHON_URL=https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
set PYTHON_INSTALLER=python-3.11.0-amd64.exe

:: Check if Python is already installed
python -V >nul 2>&1
if %errorlevel% equ 0 goto INSTALL_CANTOOLS

:: Download Python using PowerShell
echo Downloading Python 3.11.0...
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%PYTHON_URL%', '%PYTHON_INSTALLER%')"

:: Check if the file was downloaded
if not exist "%PYTHON_INSTALLER%" (
    echo Error: Failed to download Python. Check your internet connection
    pause
    exit /b 1
)

:: Install Python silently
echo Installing Python...
start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

:: Cleanup the installer
del %PYTHON_INSTALLER%

:: Refresh environment variables
echo Refreshing environment variables...
call "%~dp0RefreshEnv.cmd"

:: Verify Python installation
python -V
if %errorlevel% neq 0 (
    echo Python installation failed.
    pause
    exit /b 1
)

:INSTALL_CANTOOLS
:: Install cantools using pip
echo Installing cantools using pip...
python -m pip install cantools
if %errorlevel% neq 0 (
    echo Failed to install cantools. Try deleting your python install and running this script again.
    pause
    exit /b 1
) else (
    echo cantools installed successfully!
)

pause
endlocal
