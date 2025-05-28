@echo on

chcp 65001

call conda activate facefusion

echo 执行命令：python facefusion.py run --ui-layouts webcam --open-browser

echo facefusion直播换脸启动中，请稍等

python facefusion.py run --ui-layouts webcam --open-browser



