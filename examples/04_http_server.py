# 示例 04：HTTP 服务器
# 创建一个简单的网页来控制 LED

from machine import Pin
import network
import socket
import time

# 配置
SSID = "你的WiFi名称"
PASSWORD = "你的WiFi密码"
PORT = 80

# 初始化 LED
led = Pin(2, Pin.OUT)
led.value(1)  # 初始熄灭

def connect_wifi():
    """连接 WiFi"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print(f"连接 WiFi: {SSID}...")
        wlan.connect(SSID, PASSWORD)
        
        while not wlan.isconnected():
            time.sleep(1)
            print(".", end="")
    
    ip = wlan.ifconfig()[0]
    print(f"\nWiFi 已连接，IP: {ip}")
    return ip

def web_page():
    """生成网页"""
    led_state = "ON" if led.value() == 0 else "OFF"
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESP8266 LED 控制</title>
    <style>
        body {{ font-family: Arial; text-align: center; margin-top: 50px; }}
        h1 {{ color: #333; }}
        .btn {{ 
            padding: 15px 30px; 
            font-size: 18px; 
            margin: 10px; 
            cursor: pointer;
            border: none;
            border-radius: 5px;
        }}
        .on {{ background-color: #4CAF50; color: white; }}
        .off {{ background-color: #f44336; color: white; }}
        .status {{ font-size: 24px; margin: 20px; }}
    </style>
</head>
<body>
    <h1>ESP8266 LED 控制</h1>
    <div class="status">LED 状态: <strong>{led_state}</strong></div>
    <button class="btn on" onclick="location.href='/on'">开灯</button>
    <button class="btn off" onclick="location.href='/off'">关灯</button>
    <p><small>ESP8266 MicroPython</small></p>
</body>
</html>"""
    return html

def start_server(ip):
    """启动 HTTP 服务器"""
    addr = socket.getaddrinfo(ip, PORT)[0][-1]
    
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    
    print(f"\nHTTP 服务器启动在 http://{ip}:{PORT}")
    print("用浏览器访问上面的地址")
    
    while True:
        try:
            conn, addr = s.accept()
            print(f"\n客户端连接: {addr}")
            
            # 接收请求
            request = conn.recv(1024)
            request = str(request)
            
            # 解析请求
            if '/on' in request:
                led.value(0)  # 点亮
                print("LED ON")
            elif '/off' in request:
                led.value(1)  # 熄灭
                print("LED OFF")
            
            # 发送响应
            response = web_page()
            conn.send('HTTP/1.1 200 OK\r\n')
            conn.send('Content-Type: text/html\r\n')
            conn.send('Connection: close\r\n\r\n')
            conn.sendall(response)
            conn.close()
            
        except Exception as e:
            print(f"错误: {e}")
            conn.close()

# 主程序
if __name__ == "__main__":
    ip = connect_wifi()
    start_server(ip)
