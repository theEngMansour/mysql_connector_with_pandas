# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
# color
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
CYAN = '\033[96m'

options = Options()
options.add_argument('--headless')  # التشغيل في وضع غير مرئي
options.add_argument('--no-sandbox')  # إلغاء صندوق الرمل
options.add_argument('--disable-dev-shm-usage')  # تعطيل استخدام ذاكرة الـ shared memory

def get_data_moi():
    # Printing the introduction with colors
    print(GREEN + '--------------------------------------')
    print('EXTRACTING DATA.')
    print(YELLOW + 'by @fikra ' + CYAN + '(fikra-ye)')
    print(GREEN + '--------------------------------------' + RESET)
    url = input(CYAN + 'Input URL: ')
    region = input(CYAN + 'Input region: ')
    bransh = input(CYAN + 'Input Bransh: ')
    titles = []
    imgs = []
    regions = []
    branshs = []
    content = []

    with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as driver:
        driver.get(url)
        try:
            articles = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "linknews"))
            )

            links = [article.get_attribute("href") for article in articles]
            total_articles = len(links)

            # Use tqdm with custom bar_format and colored output
            for index, link in tqdm(enumerate(links), total=total_articles, desc="\033[92mProcessing articles\033[0m"):
                driver.get(link)
                try:
                    title = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "linknews"))
                    )
                    img = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "img_content_sub"))
                    )
                    text = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "budy_news_all"))
                    )

                    titles.append(title.text)
                    imgs.append(img.get_attribute('src'))
                    regions.append(region)
                    branshs.append(bransh)
                    content.append(text.text)

                except Exception as e:
                    print(f"Error finding elements on the article page ({link}):", e)

            if titles and imgs:
                df = pd.DataFrame({
                    "العنـوان": titles,
                    "الصـورة": imgs,
                    "الإقليــم": regions,
                    "الفرع": branshs,
                    "المحتوى": content
                })
                current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                df.to_excel(f"{region}-{bransh}-{current_time}.xlsx", index=False)
                print(GREEN + "Extracted successfully.")

        except Exception as e:
            print("Error loading articles:", e)

if __name__ == '__main__':
    get_data_moi()
