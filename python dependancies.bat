@echo off
cls

echo Upgrading pip
py -m pip install --upgrade pip

pip install --user requests -U
pip install --user pypresence -U
pip install --user psutil -U
pip install --user uptime -U 
pip install --user py-cpuinfo -U

echo  
echo  
echo  
echo  
echo Installed all packages.
pause
