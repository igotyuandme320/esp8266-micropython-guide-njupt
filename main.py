# main.py - 主程序入口
# 设备启动后会自动运行此文件

from machine import Pin
import network
import time
import gc
import config

# 初始化 LED（GPIO2，低电平点亮）
led = Pin(2, Pin.OUT)
led.value(1)  # 初始熄灭

def blink(times=1, interval=0.2):
    """LED 闪烁函数"""
    for _ in range(times):
        led.value(0)  # 点亮
        time.sleep(interval)
        led.value(1)  # 熄灭
        time.sleep(interval)

def connect_wifi():
    """连接 WiFi"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if wlan.isconnected():
        print(f"WiFi 已连接，IP: {wlan.ifconfig()[0]}")
        return True
    
    print(f"正在连接 WiFi: {config.WIFI_SSID}...")
    wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
    
    # 等待连接，最多 15 秒
    for i in range(30):
        if wlan.isconnected():
            break
        blink(1, 0.1)  # 快闪表示正在连接
        print(f"尝试连接... {i+1}/30")
    
    if wlan.isconnected():
        ip = wlan.ifconfig()[0]
        print(f"✓ WiFi 连接成功！")
        print(f"  IP 地址: {ip}")
        print(f"  子网掩码: {wlan.ifconfig()[1]}")
        print(f"  网关: {wlan.ifconfig()[2]}")
        blink(3, 0.3)  # 慢闪 3 次表示成功
        return True
    else:
        print("✗ WiFi 连接失败！")
        blink(10, 0.05)  # 快闪 10 次表示失败
        return False

def main():
    """主函数"""
    print("\n【主程序启动】")
    
    # LED 快闪 2 次表示程序开始
    blink(2, 0.1)
    
    # 连接 WiFi
    wifi_ok = connect_wifi()
    
    # 显示系统信息
    print("\n【系统信息】")
    print(f"  可用内存: {gc.mem_free()} bytes")
    print(f"  WiFi 状态: {'已连接' if wifi_ok else '未连接'}")
    
    print("\n【提示】")
    print("  按 Ctrl+C 停止程序")
    print("  按 Ctrl+D 软复位设备")
    
    # 主循环 - 可以在这里添加你的代码
    try:
        while True:
            # LED 心跳效果
            led.value(0)
            time.sleep(0.05)
            led.value(1)
            time.sleep(2)
            
            # 定期垃圾回收
            gc.collect()
            
    except KeyboardInterrupt:
        print("\n\n程序已停止")
        led.value(1)  # 熄灭 LED

# 程序入口
if __name__ == "__main__":
    main()
