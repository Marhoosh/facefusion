@echo on

chcp 65001

call conda activate facefusion

echo 执行命令：python facefusion.py run --open-browser

echo facefusion启动中，请稍等

python facefusion.py run --open-browser

pause


