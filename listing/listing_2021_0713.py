from bs4 import BeautifulSoup
import requests
import random
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_path = r'C:\Program Files\chromedriver.exe'
options = Options()
options.add_argument('--incognito')
# options.set_headless() #ブラウザ非表示で実行
driver = webdriver.Chrome(executable_path=chrome_path, options=options)


url = 'https://jp.indeed.com/jobs?q=%E8%87%AA%E7%A4%BE%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%82%92%E6%8F%90%E4%BE%9B%E3%81%99%E3%82%8Bit%E4%BC%81%E6%A5%AD&l='
# トップ画面を開く。
driver.get(url)

# ローディング待ち
sleep(3)

# タイトル部分の画像オブジェクトを取得する。
png = driver.find_element_by_id("mosaic-provider-jobcards").screenshot("t2.png")

# 画像を保存
# with open('./img.png', 'wb') as f:
#     f.write(png)


chrome_path = r'C:\Program Files\chromedriver.exe'
options = Options()
options.add_argument('--incognito')
# options.set_headless() #ブラウザ非表示で実行
driver = webdriver.Chrome(executable_path=chrome_path, options=options)

d_list = []

url = "https://jp.indeed.com/jobs?q=%E8%87%AA%E7%A4%BE%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%82%92%E6%8F%90%E4%BE%9B%E3%81%99%E3%82%8Bit%E4%BC%81%E6%A5%AD&start={}0"


for i in range(0, 2):  # page数の指定 #1-20

    target_url = url.format(i)
    print(target_url)
    try:
        driver.get(target_url)
    except AttributeError:
        print("エラー"+target_url)
        sleep(random.randint(1, 3))
    else:
        sleep(random.randint(1, 5))

        body = driver.find_element_by_xpath(
            "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div[5]/h2/a")
        a_tag = body.click()

        for con in body:
            a_tag = driver.find_element_by_tag_name("a")
            c_name = a_tag.text
            print(c_name)

            d = {
                "c_name": c_name
            }
            d_list.append(d)
            print(d_list)
        df = pd.DataFrame(d_list)
        c_r_name = "l_2021_0713_{}.csv"
        csv_name = c_r_name.format(i)
        df.to_csv(csv_name, encoding="utf_8_sig")


driver.quit()


d1_list = []
df_read = pd.read_csv(r"D:\programs\raw_wsl_py.csv", encoding="utf_8_sig")


# print(df_read.values)
# print(df_read[["c_r_name", "c_url"]])
fir_low = "{}"
for j in range(0, len(df_read.index)):
    target_low = fir_low.format(j)
    url_2 = df_read.values[int(target_low), 2]
    r2 = requests.get(url_2)
    soup = BeautifulSoup(r2.content, "html.parser")
    sleep(random.randint(1, 3))

    body_2 = soup.find("div", class_="single-wrap")
    gaiyo = body_2.find("div", class_="sidebar-meta")
    sidebars = gaiyo.find_all("div", class_="sidebar-meta-box")
    sidebar = sidebars[7]
    c_p_tag = sidebar.find("p")

    c_name = c_p_tag.text
    try:
        c_a_tag = c_p_tag.find("a")

    except AttributeError:
        c_url = "zero"
        d1 = {
            "c_url": c_url
        }
        d1_list.append(d1)

    else:
        try:
            c_url = c_a_tag.get("href")
        except AttributeError:
            c_url = "zero"
            d1 = {
                "c_url": c_url
            }
            d1_list.append(d1)
        else:
            d1 = {
                "c_name": c_name,
                "c_url": c_url
            }
            d1_list.append(d1)

df1 = pd.DataFrame(d1_list)
df1.to_csv("wsl_py.csv", encoding="utf_8_sig")
