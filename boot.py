# boot.py - 系统启动时自动执行
# 此文件在设备启动时最先执行

import gc
import time

# 打印启动信息
print("\n" + "=" * 40)
print("ESP8266 MicroPython 启动中...")
print("=" * 40)

# 垃圾回收，释放内存
gc.collect()
print(f"可用内存: {gc.mem_free()} bytes")

# 延时一下，让串口稳定
time.sleep_ms(100)
