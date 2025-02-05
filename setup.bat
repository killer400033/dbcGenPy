@echo off
setlocal

:: Define the Python download URL and target file
set PYTHON_URL=https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
set PYTHON_INSTALLER=python-3.11.0-amd64.exe

:: Download Python using PowerShell
echo Downloading Python 3.11.0...
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%PYTHON_URL%', '%PYTHON_INSTALLER%')"

:: Check if the file was downloaded
if not exist "%PYTHON_INSTALLER%" (
    echo Error: Failed to download Python.
    exit /b 1
)

:: Install Python silently
echo Installing Python...
start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

:: Cleanup the installer
del %PYTHON_INSTALLER%

:: Verify Python installation in a new shell
echo Verifying Python installation...
cmd /c "python --version"
if %errorlevel% neq 0 (
    echo Python installation failed.
    exit /b 1
) else (
    echo Python installed successfully!
)

:: Install cantools using pip
echo Installing cantools using pip...
python -m pip install cantools
if %errorlevel% neq 0 (
    echo Failed to install cantools.
    exit /b 1
) else (
    echo cantools installed successfully!
)

pause
endlocal