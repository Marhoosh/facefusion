@echo off
:: Python 虚拟环境路径
set PYTHON_PATH=%cd%\suifeng
set PYTHON_EXECUTABLE=%PYTHON_PATH%\python.exe
set PYTHONW_EXECUTABLE=%PYTHON_PATH%\pythonw.exe

:: FFmpeg 路径
set FFMPEG_PATH=%PYTHON_PATH%\Tools\ffmpeg

:: CUDA 依赖库路径
set CUDA_PATH=%PYTHON_PATH%\Library\bin
set CU_PATH=%PYTHON_PATH%\Lib\site-packages\torch\lib

:: TensorRT 路径（确保此路径包含所有必要的DLL）
set TENSORRT_PATH=%PYTHON_PATH%\Lib\site-packages\tensorrt_libs

:: 清除代理变量
set http_proxy=
set https_proxy=
set all_proxy=

:: 合并 PATH 环境变量（注意顺序）
set PATH=%TENSORRT_PATH%;%CUDA_PATH%;%CU_PATH%;%FFMPEG_PATH%;%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%

:: 可选开关
set DS_BUILD_AIO=0
set DS_BUILD_SPARSE_ATTN=0
set PYTHONWARNINGS=ignore

echo.
echo [FaceFusion] All environment variables set.
echo Launching FaceFusion UI...


:: 启动主程序
"%PYTHON_EXECUTABLE%" facefusion.py run --open-browser

pause