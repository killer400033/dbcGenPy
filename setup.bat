@echo off

:: Run git submodule update --init --recursive
echo Updating submodules...
git submodule update --init --recursive

:: Install cantools using pip
echo Installing cantools...
python3 -m pip install cantools

echo Done.
pause
