from time import sleep
import requests
import pandas as pd
import random
from bs4 import BeautifulSoup

d_list = []

url = "https://www.choicely.jp/webservice/page/{}/"
for i in range(1, 22):  # page数の指定 #1-20
    target_url = url.format(i)
    r = requests.get(target_url)
    soup = BeautifulSoup(r.content, "html.parser")
    sleep(random.randint(1, 2))

    body = soup.find("div", class_="archive-main")
    h2_tag = body.find_all("h2")
    for con in h2_tag:
        c_name = con.text
        a_tag = con.find("a")
        c_r_url = a_tag.get("href")

        d = {
            "c_r_name": c_name,
            "c_url": c_r_url
        }
        d_list.append(d)

df = pd.DataFrame(d_list)
df.to_csv("raw_wsl_py.csv", encoding="utf_8_sig")


d1_list = []
df_read = pd.read_csv("D:\programs\\raw_wsl_py.csv", encoding="utf_8_sig")


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

    except:
        c_url = "zero"
        d1 = {
            "c_url": c_url
        }
        d1_list.append(d1)

    else:
        try:
            c_url = c_a_tag.get("href")
        except:
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
