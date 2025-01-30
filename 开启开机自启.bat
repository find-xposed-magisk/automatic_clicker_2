@echo off
chcp 65001 >nul
REM 定义目标文件，假设文件名可能含中文，使用UTF - 8编码处理
REM 定义目标文件
set "sourceFile=aaa.lnk"
REM 定义当前用户自启动文件夹路径
set "userStartupFolder=C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
REM 定义所有用户自启动文件夹路径
set "allUsersStartupFolder=C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"

REM 检查目标文件是否存在
if not exist "%sourceFile%" (
    echo 文件 %sourceFile% 不存在。
    pause
    exit /b 1
)

REM 复制到当前用户自启动文件夹
if exist "%userStartupFolder%" (
    copy /y "%sourceFile%" "%userStartupFolder%"
    if %errorlevel% equ 0 (
        echo 已成功将 %sourceFile% 复制到当前用户自启动文件夹。
    ) else (
        echo 复制到当前用户自启动文件夹时出错。
    )
) else (
    echo 当前用户自启动文件夹 %userStartupFolder% 不存在。
)

REM 复制到所有用户自启动文件夹
if exist "%allUsersStartupFolder%" (
    copy /y "%sourceFile%" "%allUsersStartupFolder%"
    if %errorlevel% equ 0 (
        echo 已成功将 %sourceFile% 复制到所有用户自启动文件夹。
    ) else (
        echo 复制到所有用户自启动文件夹时出错。
    )
) else (
    echo 所有用户自启动文件夹 %allUsersStartupFolder% 不存在。
)
        echo 已成功开启开机自启动并运行clicker。
pause