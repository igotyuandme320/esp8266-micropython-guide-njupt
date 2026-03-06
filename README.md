# 南京邮电大学电工实践课程 ESP8266 MicroPython 开发指南（适用于MAC）

[![MicroPython](https://img.shields.io/badge/MicroPython-3.4+-green.svg)](https://micropython.org/)
[![ESP8266](https://img.shields.io/badge/ESP8266-ESP--12F-blue.svg)](https://www.espressif.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

从零开始使用 VS Code + MicroPico 插件开发 ESP8266（ESP-12F）的完整教程。

> 📚 **[查看 NJUPT 版本（南京邮电大学）](https://github.com/igotyuandme320/esp8266-micropython-guide-njupt/tree/master)**

## 📋 目录


---

## 💻 软件安装

### 1. 安装 VS Code

下载地址：https://code.visualstudio.com/

macOS 的安全机制有时会拦截非 App Store 的应用。
*   如果打开时提示“无法打开，因为无法验证开发者”，请尝试：
    1.  打开 **系统设置** -> **隐私与安全性**。
    2.  向下滚动到“安全性”部分。
    3.  如果看到“已阻止使用 Visual Studio Code，因为其来源不明”，点击 **“仍要打开”**。
    4.  如果在终端运行报错，可以尝试赋予执行权限：
        ```bash
        sudo xattr -rd com.apple.quarantine /Applications/Visual\ Studio\ Code.app
        ```
        (执行后输入你的开机密码，注意输入时密码不会显示)

### 2. 安装 Python

下载地址：https://www.python.org/downloads/

- 推荐版本：Python 3.10+

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

```bash
ls /dev/tty.*    #大概率为tty.usbserial-10

```

### 3. 烧录

替换 `<PORT>` 为你的串口号：

```bash
# 擦除 Flash（重要！）
esptool.py --port <PORT> erase_flash

# 刷入固件（替换 firmware.bin 为实际文件名）
esptool.py --port <PORT> --baud 460800 write_flash --flash_size=detect 0 firmware.bin
```

**示例：**
```bash
esptool.py --port /dev/tty.usbserial-110 --baud 460800 write_flash --flash_size=detect 0 esp8266-20240105-v1.22.1.bin
```

看到 `Hash of data verified.` 表示刷入成功！

---

## ⚙️ VS Code 配置

### 1. 连接开发板

1. 打开vscode
2. 插入 USB
3. 按快捷键 ```   command + shift + p ```
4. 在输入框中输入
```bash
   MicroPico: Connect
```
5. terminal显示类似
```bash
MicroPython v1.20.0 on 2023-04-26; ESP module with ESP8266
Type "help()" for more information or .help for custom vREPL commands.
>>> 
```
  看到有     >>>     的    REPL    交互框即成功

### 2. 编程与测试

1.点击左上角文件图标的EXPLORER
2.选择文件夹创建项目
3.新建   .py  文件，编写代码
4.按command + s 保存文件
5.右键文件选择
```bash
Upload file to Pico        #载入文件
Run current file on Pico   #运行文件                   
```
6.REPL终端按下 ctrl + c 停止当前程序运行
---


---



---

## 💡 示例代码

### 示例 1：LED 闪烁（课程代码）

```python
import time
from machine import Pin

led=Pin(4,Pin.OUT)        #建立LED对象，与GPIO4连接

while True:
  led.value(1)            #设置GPIO4为高电平
  time.sleep(0.5)       #设置时间间隔
  led.value(0)            #设置GPIO4为低电平
  time.sleep(0.5)       #设置时间间隔

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
