@echo off
:restart
echo ---------------------- START (%DATE:~0,2%.%DATE:~3,2% %TIME:~0,8%) ----------------------
py main.py
echo ---------------------- STOP (%DATE:~0,2%.%DATE:~3,2% %TIME:~0,8%) ----------------------
ping -n 1 127.0.0.1 > NUL
goto restart