# http://www.chukeikyo.com/fukuoka/member/ から会社名,url を抜き取り

from time import sleep
import requests
import pandas as pd
import random
from bs4 import BeautifulSoup


d_list = []
d1_list = []


url = "http://www.chukeikyo.com/fukuoka/member/"

res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")
sleep(random.randint(1, 2))

body = soup.find("div", id="cnts2box")
print(type(body))
table = body.find("table")
print(type(table))

td_tags = table.find_all("td")
print(type(td_tags))

for j, con in enumerate(td_tags, start=1):
    if j == 0:
        print("ゼロ!!!!")
    elif j % 2 == 0:
        print(type(con))
        try:
            a_tag = con.find("a")
            c_url = a_tag.get('href')
        except:
            e_c_url = "404"

            c_name = con.text
            d = {
                "c_name": c_name,
                "c_url": e_c_url
            }
            d_list.append(d)
        else:

            c_name = con.text
            d = {
                "c_name": c_name,
                "c_url": c_url
            }
            d_list.append(d)
    else:
        print("奇数")


df = pd.DataFrame(d_list)
df.to_csv("listing_2021_0811_htkk.csv", encoding="utf_8_sig")
