# https://careerconnection.jp/review/region/Hokkaido/Information-Communication/

from time import sleep
import requests
import pandas as pd
import random
from bs4 import BeautifulSoup


d_list = []
d1_list = []

url = "https://careerconnection.jp/review/region/Hokkaido/Information-Communication/?pageNo={}"
for i in range(1, 4):
    n_url = url.format(i)
    res = requests.get(n_url)
    soup = BeautifulSoup(res.content, "html.parser")
    sleep(random.randint(1, 2))

    h2_tag = soup.find_all("h2")
    for con in h2_tag:
        a_tag = con.find("a")
        r_c_url = a_tag.text
        r2_c_url = r_c_url.replace(" ", "")
        c_url = r2_c_url.replace("　", "")

        d = {
            "c_url": c_url
        }
        d_list.append(d)

df = pd.DataFrame(d_list)
df.to_csv("listing_2021_0813_ck.csv", encoding="utf_8_sig")
