# -*- coding: UTF-8 -*-
"""
__Author__ = "wahh159"
__Version__ = "1.0.1"
__Description__ = "大麦app抢票自动化"
__Created__ = 2023/12/8 9:10
"""
from time import sleep

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from config import Config
from ocr import capture_and_ocr
import random
# 加载配置信息
config = Config.load_config()

device_app_info = AppiumOptions()
# 操作系统
device_app_info.set_capability('platformName', 'Android')
# 操作系统版本
device_app_info.set_capability('platformVersion', '14')
# 设备名称
device_app_info.set_capability('deviceName', '69b6b7a4')
# app package
device_app_info.set_capability('appPackage', 'cn.damai')
# app activity name
device_app_info.set_capability('appActivity', '.launcher.splash.SplashMainActivity')
# 使用unicode输入
device_app_info.set_capability('unicodeKeyboard', True)
# 隐藏键盘
device_app_info.set_capability('resetKeyboard', True)
# 不重置app
device_app_info.set_capability('noReset', True)
# 超时时间
device_app_info.set_capability('newCommandTimeout', 6000)

# 使用uiautomator2驱动
device_app_info.set_capability('automationName', 'UiAutomator2')


# 连接appium server，server地址查看appium启动信息
driver = webdriver.Remote(config.server_url, options=device_app_info)

# sleep(5)

# 设置等待时间，等待1s
driver.implicitly_wait(0.1)
# 空闲时间10ms,加速
driver.update_settings({"waitForIdleTimeout": 0.1})


def handle_order(driver, config):
    if driver.find_elements(by=By.ID, value='recycler_main') and config.users is not None:
        text_name_list=driver.find_elements(by=By.ID, value='text_name')
        for text_name in text_name_list:
            if text_name.text in config.users:
                text_name.click()
    # 提交订单
    if config.if_commit_order:                  
        if driver.find_elements(by=AppiumBy.ANDROID_UIAUTOMATOR,
                            value='new UiSelector().text("提交订单")'):
            print('handleOrder')
            # driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("提交订单")').click()
            # return True  # 返回 True 表示提交订单成功
            driver.back()
            return False  # 返回 False 表示提交订单失败
            
    driver.back()
    return False  # 返回 False 表示提交订单失败

def ticket_price_num(driver,config,priceIndex,numSelect):
    # 票价选择
    if driver.find_elements(by=By.ID, value='project_detail_perform_price_flowlayout'):       
        driver.find_element(by=By.XPATH,
                                        value='(//android.widget.TextView[@resource-id="cn.damai:id/item_text"])[{}]'.format(config.priceList[priceIndex]+config.dateLen)).click()
        
        print('票价选择22',config.priceList[priceIndex]+config.dateLen)
    # 数量选择
    if driver.find_elements(by=By.ID, value='layout_num') and config.users is not None:
        for i in range(len(config.users) - 1):
            driver.find_element(by=By.ID, value='img_jia').click()
            print('数量选择22')
        num_el=driver.find_element(by=By.ID, value='tv_num')
        if num_el and num_el.text and num_el.text[0]==str(len(config.users)):
            print('张数',num_el.text)
            numSelect=True   
    return numSelect

def selset(driver,config):
    first=True #第一次进入
    comfirm=False #是否确认了
    priceIndex=0    
    dateIndex=0
    numSelect=False #选的数量是否正确
        
    while not comfirm:
        if driver.find_elements(by=By.ID, value='btn_buy'):
            buy_btn=driver.find_element(by=By.XPATH, value='//android.widget.LinearLayout[@resource-id="cn.damai:id/btn_buy"]/android.widget.TextView')
            print('btn_buyssssssssss',buy_btn)
            if buy_btn.text !='提交缺货登记' and (not first) and numSelect:
                buy_btn.click()
                comfirm=True
            else:
                if not first:
                    priceIndex= (priceIndex+1) % len(config.priceList)
                if (priceIndex==0 or first) and config.dateLen>1:
                    if not first:
                        dateIndex= (dateIndex+1) % len(config.dateList)
                    if driver.find_elements(by=By.ID, value='layout_perform_view'):
                        print('日期选择2',dateIndex)   
                        driver.find_element(by=By.XPATH,value='(//android.widget.LinearLayout[@resource-id="cn.damai:id/ll_perform_item"])[{}]'.format(config.dateList[dateIndex])).click()
                    numSelect=ticket_price_num(driver,config,priceIndex,numSelect)
                else:
                    # print('priceIndex',priceIndex)
                    numSelect=ticket_price_num(driver,config,priceIndex,numSelect)

                first=False
    if comfirm:
        comfirmSuccess = handle_order(driver, config)
    return comfirmSuccess
    

                            
                        
while driver.find_elements(by=By.XPATH,
                           value='//android.widget.FrameLayout[@resource-id="cn.damai:id/trade_project_detail_purchase_status_bar_container_fl"]'):
    # 定义需要截取的区域的坐标
    left, top, right, bottom = 568, 2290, 622, 2340

    # 调用函数获取文字
    bot_btn= capture_and_ocr(driver, left, top, right, bottom)
    
    # 立即购买
    if '立' in bot_btn or '缺' in bot_btn :
        driver.tap([(606, 2301)])

        comfirmSuccess=False
        while not comfirmSuccess:
            comfirmSuccess=selset(driver,config)      
    else:
        # 模拟下拉刷新
        driver.swipe(500, 400, 500, 2000, 300)
        sleep(0.5)

driver.quit()
