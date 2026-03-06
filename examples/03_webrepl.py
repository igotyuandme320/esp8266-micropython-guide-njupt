# 示例 03：WebREPL 配置
# 启用无线 REPL，无需 USB 线即可调试

import webrepl
import network
import time

# 配置（首次使用后会保存到 webrepl_cfg.py）
PASSWORD = "123456"  # 设置 WebREPL 密码

def setup_wifi():
    """确保 WiFi 已连接"""
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print("请先连接 WiFi")
        return False
    print(f"WiFi 已连接: {wlan.ifconfig()[0]}")
    return True

def start_webrepl():
    """启动 WebREPL"""
    print("\n正在启动 WebREPL...")
    webrepl.start(password=PASSWORD)
    print("✓ WebREPL 已启动！")
    print(f"  密码: {PASSWORD}")
    
    # 获取 IP 地址
    wlan = network.WLAN(network.STA_IF)
    ip = wlan.ifconfig()[0]
    print(f"\n连接方式:")
    print(f"  1. 访问 http://micropython.org/webrepl/")
    print(f"  2. 在地址栏输入: ws://{ip}:8266")
    print(f"  3. 输入密码连接")

# 主程序
if __name__ == "__main__":
    if setup_wifi():
        start_webrepl()
    else:
        print("无法启动 WebREPL：WiFi 未连接")
