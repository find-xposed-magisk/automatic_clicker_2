@echo off
chcp 65001 >nul
REM 定义目标文件
set "sourceFile=aaa.lnk"
REM 定义当前用户自启动文件夹路径
set "userStartupFolder=C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
REM 定义所有用户自启动文件夹路径
set "allUsersStartupFolder=C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"

REM 检查当前用户自启动文件夹中目标文件是否存在并删除
if exist "%userStartupFolder%\%sourceFile%" (
    del /q "%userStartupFolder%\%sourceFile%"
    if %errorlevel% equ 0 (
        echo 已成功从当前用户自启动文件夹中删除 %sourceFile%。
    ) else (
        echo 从当前用户自启动文件夹删除 %sourceFile% 时出错。
    )
) else (
    echo 当前用户自启动文件夹中不存在 %sourceFile%。
)

REM 检查所有用户自启动文件夹中目标文件是否存在并删除
if exist "%allUsersStartupFolder%\%sourceFile%" (
    del /q "%allUsersStartupFolder%\%sourceFile%"
    if %errorlevel% equ 0 (
        echo 已成功从所有用户自启动文件夹中删除 %sourceFile%。
    ) else (
        echo 从所有用户自启动文件夹删除 %sourceFile% 时出错。
    )
) else (
    echo 所有用户自启动文件夹中不存在 %sourceFile%。
)

pause