# https://callingood.com/office/

from time import sleep
import requests
import pandas as pd
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
d_list = []

chrome_path = r'D:\chromedriver\chromedriver_win32\chromedriver.exe'
options = Options()
options.add_argument('--incognito')
# options.set_headless() #ブラウザ非表示で実行
driver = webdriver.Chrome(executable_path=chrome_path, options=options)


url = 'https://callingood.com/office/'
driver.get(url)
sleep(random.randint(1, 2))


def ax1(ken):
    jump_ken = driver.find_element_by_id(ken)
    jump_ken
    clearfix = t_ken.find_element_by_class_name("clearfix")
    companyNames = clearfix.find_elements_by_class_name("companyNames")

    for con in companyNames:
        a_tag = con.find_element_by_tag_name("a")
        t_url = a_tag.get_attribute("href")
        print(t_url)

        d = {
            "t_url": t_url
        }
        d_list.append(d)


kens = ["jump_hokkaidou", "jump_miyagi", "jump_yamagata", "jump_tochigi", "jump_gunma", "jump_saitama", "jump_chiba", "jump_tokyo", "jump_kanagawa", "jump_niigata", "jump_nagano", "jump_isikawa", "jump_gifu", "jump_sizuoka", "jump_aichi", "jump_kyouto", "jump_osaka", "jump_hyougo", "jump_okayama", "jump_hirosima", "jump_ehime", "jump_fukuoka", "jump_okinawa"]
for j in range(0, len(kens)):
    print(j)
    t_ken = kens[j]
    ax1(t_ken)

df = pd.DataFrame(d_list)
df.to_csv("listing_2021_0813_cg_1.csv", encoding="utf_8_sig")


d1_list = []
df_read = pd.read_csv("D:\programs\listing_2021_0813_cg_1.csv", encoding="utf_8_sig")
data_np = np.asarray(df_read)
print("データ読み込み完了")
for row in data_np:
    url_3 = row[1]
    print(url_3)
    res = requests.get(url_3)
    soup = BeautifulSoup(res.content, "html.parser")
    sleep(random.randint(1, 3))

    h1_tag = soup.find("h1")
    section = soup.find("section", class_="section")
    table = section.find("table", class_="infotable")
    tbody = table.find("tbody")
    td_tags = tbody.find_all("td")
    td_tag = td_tags[1]
    r_c_url = td_tag.text
    c_url = r_c_url.replace("※HPからのお問合せの場合は、コーリングッドを見てお問合せしたとお伝えください", "")
    c_name = h1_tag.text

    d1 = {
        "c_name": c_name,
        "c_url": c_url
    }
    d1_list.append(d1)

df_1 = pd.DataFrame(d1_list)
df_1.to_csv("listing_2021_0813_cg_2.csv", encoding="utf_8_sig")
