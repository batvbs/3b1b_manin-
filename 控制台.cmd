@echo off&chcp 65001 >nul&setlocal enabledelayedexpansion
rem 项目位置 https://github.com/batvbs/3b1b_manin-

set 不申请管理员权限=1
rem 如果打算以管理员权限运行, 值留空

set manin所在路径=
rem 如果manin和本程序位于同一目录, 值留空

set 默认脚本=example_scenes.py
rem 请输入相对路径或绝对路径, 可留空

set 默认输出设置=-pl
rem -p预览 -l低画质 -s 最后帧  -n 数字 跳到第n个动画 -f 在查找器中显示文件 可留空

if not DEFINED 不申请管理员权限 (fsutil dirty query "%systemdrive%" 1>nul 2>nul || (mshta vbscript:CreateObject^("Shell.Application"^).ShellExecute^("""cmd.exe""","/c %~s0",,"runas",1^)^(window.close^)&&exit))
if DEFINED manin所在路径 (cd /d "%manin所在路径%" || exit) else (cd /d "%~dp0")
echo Manin控制台 [版本 1.0] 作者 batvbs
echo 输入h查看帮助
if DEFINED 默认脚本 (echo ^>^>%默认脚本%&set "命令=%默认脚本%"&goto 11)

:1
set 命令=
echo.
set /p "命令=>>"
set 命令2=%命令%

:11
if not DEFINED 命令 goto 1
if "%命令%" == "q" cmd
if "%命令%" == "h" goto h
if "%命令%" == "c" cls&goto 1
call :2 %命令%
goto 1

:2
if not exist "%~1" goto 21
title manim %~1
set 脚本=%~1
set aa=0
echo ---------- %~1
set 序号_=1&set 类名_=1
for /f "delims=" %%a in ('set 序号_') do set %%a=
for /f "delims=" %%a in ('set 类名_') do set %%a=
for /f "eol=  delims=:" %%a in ('find "class " "%~1"') do (set ab=%%a
  set ab=!ab:(= !
  for /f "eol=- tokens=2 delims= " %%b in ("!ab!") do (
    set /a aa+=1
    set 序号_!aa!=%%b
    set 类名_%%b=%%b
    echo [!aa!] %%b))
echo 请输入序号或类名
exit /b

:21
set 命令=
set 输出=%~2
if "%输出%" == "" set 输出=%默认输出设置%
if DEFINED 序号_%~1 set 命令=!序号_%~1!
if DEFINED 类名_%~1 set 命令=!类名_%~1!
if DEFINED 命令 (
  title manim %脚本% %命令% %输出%
  echo ---- manim %脚本% %命令% %输出%
  python manim.py "%脚本%" %命令% %输出%
  ) else (echo  '%~1' 不是 序号 或 类名，也不是 可运行的.py程序文件)
exit /b

:h
echo 可以输入序号或类名, 或Manin的.py脚本文件
echo h帮助 q退出 c清屏 ↑↓键历史记录
exit /b
