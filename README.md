# ESP8266 MicroPython 开发指南

[![MicroPython](https://img.shields.io/badge/MicroPython-3.4+-green.svg)](https://micropython.org/)
[![ESP8266](https://img.shields.io/badge/ESP8266-ESP--12F-blue.svg)](https://www.espressif.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

从零开始使用 VS Code + MicroPico 插件开发 ESP8266（ESP-12F）的完整教程。

> 📚 **[查看 NJUPT 版本（南京邮电大学）](https://github.com/igotyuandme320/esp8266-micropython-guide-njupt/tree/master)**

## 📋 目录

- [硬件准备](#硬件准备)
- [接线图](#接线图)
- [软件安装](#软件安装)
- [刷入固件](#刷入固件)
- [VS Code 配置](#vs-code-配置)
- [项目结构](#项目结构)
- [快速开始](#快速开始)
- [示例代码](#示例代码)
- [进阶功能](#进阶功能)
- [常见问题](#常见问题)

---

## 🔧 硬件准备

| 物品 | 说明 |
|------|------|
| ESP-12F 模块 | ESP8266 核心模块 |
| USB 转 TTL 模块 | CH340 或 CP2102 芯片 |
| 杜邦线 | 母对母或公对母若干 |
| 面包板（可选） | 方便接线 |

**注意**：ESP-12F 工作电压为 **3.3V**，切勿使用 5V！

---

## 🔌 接线图

### 烧录模式接线

```
USB-TTL          ESP-12F
-------          -------
TX        ---->  RX (GPIO3)
RX        ---->  TX (GPIO1)
GND       ---->  GND
3.3V      ---->  VCC
3.3V      ---->  EN (CH_PD)
GND       ---->  GPIO0  (烧录时短接，运行时不接)
```

### 运行模式接线

烧录完成后，**断开 GPIO0 和 GND 的连接**，重新上电即可运行程序。

---

## 💻 软件安装

### 1. 安装 VS Code

下载地址：https://code.visualstudio.com/

### 2. 安装 Python

下载地址：https://www.python.org/downloads/

- 推荐版本：Python 3.10+
- **Windows 用户**：安装时勾选 "Add Python to PATH"

### 3. 安装 esptool

```bash
pip install esptool
```

### 4. 安装 MicroPico 插件

1. 打开 VS Code
2. 点击左侧扩展图标（或按 `Ctrl+Shift+X`）
3. 搜索 **MicroPico**
4. 点击安装

---

## 🔥 刷入固件

### 1. 下载固件

从 [MicroPython 官网](https://micropython.org/download/esp8266/) 下载最新固件：

- 选择 **ESP8266 generic** 
- 下载 `.bin` 文件

### 2. 确认串口号

**macOS/Linux：**
```bash
ls /dev/tty.*
# 或
ls /dev/cu.*
```

**Windows：**
```cmd
mode COM:
```

### 3. 进入烧录模式

1. 将 GPIO0 接到 GND
2. 重新插拔 USB（或按复位键）
3. 松开 GPIO0（此时已进入烧录模式）

### 4. 擦除并刷入

替换 `<PORT>` 为你的串口号：

```bash
# 擦除 Flash（重要！）
esptool.py --port <PORT> erase_flash

# 刷入固件（替换 firmware.bin 为实际文件名）
esptool.py --port <PORT> --baud 460800 write_flash --flash_size=detect 0 firmware.bin
```

**示例：**
```bash
# macOS
esptool.py --port /dev/tty.usbserial-110 --baud 460800 write_flash --flash_size=detect 0 esp8266-20240105-v1.22.1.bin

# Windows
esptool.py --port COM3 --baud 460800 write_flash --flash_size=detect 0 esp8266-20240105-v1.22.1.bin
```

看到 `Hash of data verified.` 表示刷入成功！

---

## ⚙️ VS Code 配置

### 1. 连接开发板

1. 断开 GPIO0 和 GND 的连接（运行模式）
2. 重新插拔 USB
3. VS Code 左下角会显示 **"Pico Disconnected"**
4. 点击 → 选择你的串口 → 等待连接
5. 显示 **"Pico Connected"** 绿色状态即成功

### 2. 打开 REPL

- 按 `Ctrl+Shift+P`
- 输入 **"MicroPico: Open REPL"**
- 看到 `>>>` 提示符即可开始交互

### 3. 常用快捷键

| 操作 | 快捷键 |
|------|--------|
| 上传当前文件 | `Ctrl+Shift+P` → Upload current file |
| 上传项目 | `Ctrl+Shift+P` → Upload project |
| 打开 REPL | `Ctrl+Shift+P` → Open REPL |
| 软复位 | REPL 中按 `Ctrl+D` |

---

## 📁 项目结构

```
esp8266-micropython-guide/
├── README.md              # 本文件
├── main.py               # 主程序入口
├── boot.py               # 启动配置（网络、初始化）
├── config.py             # 配置文件（WiFi 密码等）
├── lib/                  # 第三方库
│   └── ...
├── examples/             # 示例代码
│   ├── 01_blink.py      # LED 闪烁
│   ├── 02_wifi.py       # WiFi 连接
│   ├── 03_webrepl.py    # WebREPL 配置
│   └── 04_http_server.py # HTTP 服务器
└── .gitignore           # Git 忽略文件
```

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/你的用户名/esp8266-micropython-guide.git
cd esp8266-micropython-guide
```

### 2. 修改配置

编辑 `config.py`，填入你的 WiFi 信息：

```python
WIFI_SSID = "你的WiFi名称"
WIFI_PASSWORD = "你的WiFi密码"
```

### 3. 上传到开发板

1. VS Code 连接串口
2. 右键点击 `main.py` → **Upload to Pico**
3. 或者按 `Ctrl+Shift+P` → **MicroPico: Upload current file**

### 4. 运行

**方式一：REPL 中运行**
```python
exec(open("main.py").read())
```

**方式二：软复位自动运行**
- REPL 中按 `Ctrl+D`
- 或重新插拔 USB

---

## 💡 示例代码

### 示例 1：LED 闪烁

```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)  # GPIO2，板载 LED

while True:
    led.value(0)  # 点亮（低电平有效）
    time.sleep(0.5)
    led.value(1)  # 熄灭
    time.sleep(0.5)
```

### 示例 2：WiFi 连接

```python
import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("SSID", "PASSWORD")

while not wlan.isconnected():
    time.sleep(1)

print("IP:", wlan.ifconfig()[0])
```

更多示例见 [`examples/`](examples/) 目录。

---

## 🎯 进阶功能

- [ ] WebREPL - 无线 REPL 调试
- [ ] MQTT - 物联网消息通信
- [ ] HTTP Server - 网页控制界面
- [ ] OTA 升级 - 无线固件更新
- [ ] Deep Sleep - 低功耗模式

---

## ❓ 常见问题

### Q: 刷固件时提示 "Failed to connect to ESP8266"

A: 检查 GPIO0 是否正确接地，重新插拔 USB 重试。

### Q: 上传文件后没有自动运行

A: 确保文件名为 `main.py`，软复位（`Ctrl+D`）或重新上电。

### Q: WiFi 连接失败

A: 检查 `config.py` 中的 SSID 和密码，确保是 2.4GHz 网络。

### Q: MicroPico 无法连接

A: 检查串口是否被其他程序占用（如其他终端），关闭后重试。

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 🔗 参考链接

- [MicroPython 官方文档](https://docs.micropython.org/en/latest/esp8266/quickref.html)
- [ESP8266 技术规格](https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf)
- [MicroPico 插件](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go)
