from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import random
import requests
from bs4 import BeautifulSoup
# import datetime
# import os
# import re
# from gspread_dataframe import get_as_dataframe, set_with_dataframe

chrome_path = r'C:\Program Files\chromedriver.exe'
options = Options()
options.add_argument('--incognito')
options.set_headless()  # ブラウザ非表示で実行
driver = webdriver.Chrome(executable_path=chrome_path, options=options)

d1_list = []
d_list = []

kens = ["40_fukuoka", "41_saga", "42_nagasaki", "43_kumamoto",
        "44_ooita", "45_miyazaki", "46_kagoshima", "47_okinawa"]
for ken in kens:
    url = "https://www.biz.ne.jp/list/industry/"+ken+"/?datacnt={}0&pref_md=spref&key_goods=17#list"

    for i in range(0, 9):  # page数の指定 #1-20
        target_url = url.format(i)
        print(target_url)

# 型番抜き出し
        r = requests.get(target_url)
        soup = BeautifulSoup(r.text)
        sleep(random.randint(1, 3))
        try:
            body = soup.find("div", class_="list_in")
            contents = body.find_all("li", class_="result_box")
        except AttributeError:
            pass
        else:

            for content in contents:
                h3_tag = content.find("h3")
                a_tag = h3_tag.find("a").text
                print(a_tag)

                # kataban = clear_1.replace("\n","")

                d1 = {
                    "名前": a_tag
                }
                d1_list.append(d1)
            print("型番抜き出し完了")

    df = pd.DataFrame(d1_list)
    df.to_csv("kai"+ken+".csv", encoding="utf_8_sig")  # csv出力
    d1_list.clear()

driver.quit()
