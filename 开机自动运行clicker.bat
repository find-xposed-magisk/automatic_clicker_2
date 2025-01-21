@echo off
start "" "%~dp0clicker.exe"
ping 127.0.0.1 -n 4 >nul
echo Set WshShell = CreateObject("WScript.Shell") > send_f10.vbs
echo WshShell.SendKeys "{F10}" >> send_f10.vbs
cscript send_f10.vbs
del send_f10.vbs