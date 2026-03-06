# 示例 02：WiFi 连接
# 连接 WiFi 网络并显示 IP 地址

import network
import time

# WiFi 配置（可以改成你自己的）
SSID = "你的WiFi名称"
PASSWORD = "你的WiFi密码"

def connect_wifi(ssid, password, timeout=15):
    """
    连接 WiFi
    
    参数:
        ssid: WiFi 名称
        password: WiFi 密码
        timeout: 超时时间（秒）
    
    返回:
        成功返回 IP 地址，失败返回 None
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    # 检查是否已连接
    if wlan.isconnected():
        print(f"WiFi 已连接: {wlan.ifconfig()[0]}")
        return wlan.ifconfig()[0]
    
    print(f"正在连接 WiFi: {ssid}...")
    wlan.connect(ssid, password)
    
    # 等待连接
    for i in range(timeout):
        if wlan.isconnected():
            break
        print(f"连接中... {i+1}/{timeout}")
        time.sleep(1)
    
    if wlan.isconnected():
        ip = wlan.ifconfig()[0]
        print(f"\n✓ 连接成功！")
        print(f"  IP 地址: {ip}")
        print(f"  子网掩码: {wlan.ifconfig()[1]}")
        print(f"  网关: {wlan.ifconfig()[2]}")
        print(f"  DNS: {wlan.ifconfig()[3]}")
        return ip
    else:
        print("\n✗ 连接失败！")
        print("  请检查 WiFi 名称和密码")
        return None

# 主程序
if __name__ == "__main__":
    ip = connect_wifi(SSID, PASSWORD)
    
    if ip:
        print(f"\n可以使用 http://{ip} 访问设备")
