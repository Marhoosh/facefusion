#!/usr/bin/env python3
import os
import time
import pyfiglet
print()
print()
print()
print()
# ===== 美观启动展示 =====
import pyfiglet

# ===== 美观启动展示 =====
big_text = pyfiglet.figlet_format("FaceFusion", font="slant")

# 定义美观的展示格式
banner = f"""
********************************************************************************
{big_text.rstrip()}
********************************************************************************

              FaceFusion3.2.0 一键启动包

********************************************************************************

   微信公众号：随风mar  |   抖音：随风mar   ｜  B站：随风mar

   疑难解答、远程协助、技术支持服务 ＋ 微信: workTech168

              Facefusion交流QQ群：740529265


********************************************************************************
"""

# 打印结果
print(banner)
time.sleep(1.5)


os.environ['OMP_NUM_THREADS'] = '1'

from facefusion import core

if __name__ == '__main__':
	core.cli()
