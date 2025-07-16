#!/usr/bin/env python3
import os
import time
import pyfiglet
from colorama import init, Fore, Back, Style

# 初始化 colorama（Windows 必须调用 init()）
init(autoreset=True)

print("\n" * 4)  # 空行

# ===== 美观启动展示 =====
big_text = pyfiglet.figlet_format("FaceFusionPro", font="slant")

# 定义美观的展示格式（使用 Fore.COLOR 设置颜色）
banner = f"""
{Fore.CYAN}********************************************************************************
{Fore.YELLOW}{big_text.rstrip()}
{Fore.CYAN}********************************************************************************

{Fore.GREEN}              FaceFusionPro3.3.2 一键启动整合包

{Fore.CYAN}********************************************************************************

{Fore.WHITE}   微信公众号：{Fore.MAGENTA}随风mar  {Fore.WHITE}|   抖音：{Fore.MAGENTA}随风mar   {Fore.WHITE}｜  B站：{Fore.MAGENTA}随风mar


{Fore.YELLOW}   疑难解答  |   远程协助  |   技术支持服务   ＋ 微信: workTech168


{Fore.GREEN}              Facefusion交流QQ群：740529265

{Fore.CYAN}********************************************************************************

{Fore.RED}免责声明【本软件仅供学习、娱乐，不可用于一切违反法律的行为，如使用则用户同意个人负责，与资源发布者无关】
{Fore.RED}版权声明【本软件来自开源项目facefusion，由公众号“随风mar”打包整合，版权归原作者所有】

{Fore.CYAN}********************************************************************************
{Fore.YELLOW}软件正在启动中，预计需要10秒钟左右，请稍等......
"""

# 打印结果
print(banner)
time.sleep(1.5)

os.environ['OMP_NUM_THREADS'] = '1'

from facefusion import core

if __name__ == '__main__':
    core.cli()
