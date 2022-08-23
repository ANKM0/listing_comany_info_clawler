# https://web-kanji.com/search/web-marketing から会社名,urlを抜き出し
# WEBマーケティングに特化した制作会社さんをお探ししたところ


from time import sleep
import requests
import pandas as pd
import random
from bs4 import BeautifulSoup
import numpy as np

d_list = []


def wk_requests(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    sleep(random.randint(1, 2))

    body = soup.find("div", id="search-result")
    companies = body.find("div", class_="companies")

    a_tags = companies.select('a[href]')
    for con in a_tags:
        t_url = con.get('href')

        # /contact と tel:03-6457-3550 を除外
        if t_url == "/contact":
            print("排除1")
            # pass
        elif t_url == "tel:03-6457-3550":
            print("排除2")
            # pass
        else:
            d = {
                "c_url": t_url
            }
            d_list.append(d)
            print("リスト完了")
    print("データ完了")


# 1ページ目と2ページ目～ の仕様が違ったので url_1,r_url_2で分けた
url_1 = "https://web-kanji.com/search/web-marketing"
wk_requests(url_1)

r_url_2 = "https://web-kanji.com/search/web-marketing/page/{}"
for i in range(2, 41):
    url_2 = r_url_2.format(i)
    wk_requests(url_2)


# 一回　csvに出力
df = pd.DataFrame(d_list)
df.to_csv("kari.csv", encoding="utf_8_sig")


d1_list = []
df_read = pd.read_csv("D:\programs\kari.csv", encoding="utf_8_sig")

# まとめたcsvから1行ずつ取り出してbs4で解析

# import numpy as np
# data_np = np.asarray(df_read)
# for row in data_np:
#     pass
# data = pd.DataFrame(data_np)
# print(data)

data_np = np.asarray(df_read)
print("データ読み込み完了")
for row in data_np:
    url_3 = row[1]
    r2 = requests.get(url_3)
    soup_2 = BeautifulSoup(r2.content, "html.parser")
    sleep(random.randint(1, 3))

# 会社名,url 集める
    company_content = soup_2.find("div", class_="company-content")
    cdis = company_content.find("dl", class_="company-data is-narrow")
    dd_tag = cdis.find("dd")
    c_name = dd_tag.text
    print("会社名完了")

    c_a_tags = cdis.select('a[href]')
    for con_2 in c_a_tags:
        c_url = con_2.get('href')
    print("url完了")

    d1 = {
        "t_url": url_3,
        "c_name": c_name,
        "c_url": c_url
    }
    d1_list.append(d1)
    print("リスト完了")

df = pd.DataFrame(d1_list)
df.to_csv("listing_2021_0729_wk.csv", encoding="utf_8_sig")
