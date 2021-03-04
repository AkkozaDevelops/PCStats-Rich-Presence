@echo off
cls

echo Upgrading pip
py -m pip install –upgrade pip

pip install --user requests
pip install --user pypresence
pip install --user psutil
pip install --user uptime
pip install --user py-cpuinfo

echo  
echo  
echo  
echo  
echo Installed all packages.
pause
