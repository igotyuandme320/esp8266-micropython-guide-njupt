# 示例 01：LED 闪烁
# 最基础的硬件控制示例

from machine import Pin
import time

# GPIO2 是 ESP-12F 的板载 LED（低电平点亮）
led = Pin(2, Pin.OUT)

print("LED 闪烁示例 - 按 Ctrl+C 停止")

try:
    while True:
        led.value(0)  # 点亮 LED（GPIO2 低电平有效）
        print("LED ON")
        time.sleep(0.5)
        
        led.value(1)  # 熄灭 LED
        print("LED OFF")
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("\n程序已停止")
    led.value(1)  # 确保 LED 熄灭
