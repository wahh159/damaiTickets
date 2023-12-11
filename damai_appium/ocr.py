"""
__Author__ = "wahh159"
__Version__ = "1.0.0"
__Description__ = "大麦app抢票自动化"
__Created__ = 2023/12/8 9:10
"""

from appium import webdriver
import pytesseract
from PIL import Image
import time
def capture_and_ocr(driver, left, top, right, bottom):
    start_time = time.time()  # 记录开始时间
    # 截图并保存为图片文件
    screenshot_path = "screenshot2.png"
    driver.save_screenshot(screenshot_path)

    # 读取截图文件并截取指定区域
    image = Image.open(screenshot_path)
    cropped_image = image.crop((left, top, right, bottom))
    pytesseract.pytesseract.tesseract_cmd = 'G:\\tesseractOcr\\\\tesseract.exe'
    # 使用 OCR 获取文字
    custom_config = r'--oem 1 --psm 6'
    text = pytesseract.image_to_string(cropped_image, lang='chi_sim', config=custom_config)
    print('zzzzzzzz',text)
    end_time = time.time()  # 记录结束时间
    elapsed_time = end_time - start_time  # 计算时间差

    print(f"OCR 耗时：{elapsed_time} 秒")
    return text