# 大麦抢票脚本 V1.0

## 准备工作

### 1. 配置环境

#### 1.1 java jdk

#### 1.2 Android sdk

#### 1.3 node

#### 1.4 python3 环境

### 2 安装所需要的工具和依赖

在命令窗口输入如下指令

```shell
pip install selenium
```

```shell
pip install pytesseract
```

pytesseract 还需要安装，自己去 github 搜仓库安装

```shell
pip install pillow
```

```shell
npm install -g appium
```

```shell
  pip install Appium-Python-Client
```

```shell
  npm install appium-uiautomator2-driver
```

uiautomator2 可能报错，就去环境变量添加 APPIUM_SKIP_CHROMEDRIVER_INSTALL 为 true

### 3. 修改配置文件

在运行程序之前，需要先修改`config.json`文件。观演的人员、日期数组（第几个）、日期长度、价格数组（第几个）等。

#### 3.1 文件内容说明

- `server_url` 服务地址一般不用改
- `users`为观演人的姓名，**观演人需要用户在手机大麦 APP 中先填写好，然后再填入该配置文件中**，**待修改**
- `if_commit_order`为是否要自动提交订单，**改成 true**
- `dateList`为场次日期数组，要选的第几个日期，**待修改**
- `dateLen`为场次日期数组长度，**待修改**
- `priceList`为票档的价格数组，要选的第几个价格，**待修改**

### 4.运行程序

#### 4.1 启动 appium

手机开发者模式，打开 usb 安装和调试，手机数据线连上电脑，打开准备抢票的页面，如下
<img src="damai_appium/screenshot.png" width="50%" height="50%" />

#### 4.2 启动 appium

```shell
appium
```

类似出现下面的
Available drivers:- uiautomator2 (automationName 'UiAutomator2')
就可以了
[Appium] Welcome to Appium v2.2.1 (REV 2176894a5be5da17a362bf3f20678641a78f4b69)
[Appium] Attempting to load driver uiautomator2...
[Appium] Requiring driver at /Users/chenweicheng/Documents/xcode/node_modules/appium-uiautomator2-driver
[Appium] Appium REST http interface listener started on http://0.0.0.0:4723
[Appium] You can provide the following URLs in your client code to connect to this server:
[Appium] http://127.0.0.1:4723/ (only accessible from the same host)
[Appium] Available drivers:
[Appium] - uiautomator2 (automationName 'UiAutomator2')

运行程序开始抢票，进入命令窗口，执行如下命令：

```shell
cd damai_appium
python damaiApp.py
```

如果报错或者缺了啥依赖就下就完了

不商用，半成品，仅供学习参考而已，可以自己优化一下，自己研究研究
优化后已经可以跳过弹窗和滑块了，这是测试效果
<img src="damai_appium/1.gif" width="50%" height="50%" />

![image](https://github.com/wahh159/damaiTickets/assets/34958368/93df5e3a-ab5c-4cc2-b6dc-d15bb1cb3ffb)
