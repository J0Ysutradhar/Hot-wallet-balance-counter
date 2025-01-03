from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import datetime
driver = webdriver.Chrome()

#Replace these wallet address with your own address
js_usernames = [
    "pcdogh.tg", "bybit_suppor.tg", "7937417952.tg", "mahojabin090.tg", "jahidur19.tg",
    "h2on06.tg", "6517864089.tg", "binanc_toke.tg", "moneysoul1.tg", "kop_23456.tg",
    "mulakop.tg", "ramkop123.tg", "kopmama1234.tg", "texiumq.tg", "sxnium.tg",
    "ramthapkup.tg", "scnium.tg", "oxygen_hacker.tg", "7512938900.tg", "metasoul77.tg",
    "jsmetasoul.tg", "durga0_0.tg", "jdmm999.tg", "cs2skintop.tg", "xepsiam.tg",
    "emptysoul77.tg", "tentifires.tg", "xenomorph234.tg", "xepsiam1.tg", "ndearium.tg",
    "rentunium.tg", "vetarium.tg", "kallu_123456.tg", "dipsd77.tg", "gptopena.tg",
    "dev969696.tg", "jomonatv2.tg", "deshtv77.tg", "7547148001.tg", "bhaskarbro77.tg",
    "bangladesh852.tg", "hungrysoul77.tg", "refersell1234.tg", "djkallu12345.tg",
    "xenicius.tg", "bendradox.tg", "foxzium.tg", "cross_wallets.tg","355348.village.hot.tg"
]


total = []
count=0
for user in js_usernames:
    try:
        url = f"https://hotscan.org/wallet/{user}"
        driver.get(url)
        time.sleep(1)

        balance_element = driver.find_element(By.XPATH, "//h2[@class='sc-gueXAH VAnti']")
        balance = balance_element.text

        balance_float = float(balance)
        total.append(balance_float)

        print(f"{user} Balance:", balance_float)
        count=count+1

    except Exception as e:
        # print(f"Error fetching balance for {user}: {e}")
        print(f"|:>|||||||||||||==================>Error fetching balance for '{user}' Try manually with this link {url}")
time=datetime.datetime.now()
driver.quit()
hot= sum(total)
with open("JShot.txt", "a") as f:
    f.write(str(hot)+f" HOT token at {time}" "\n")
print("<<-------------------------------------------------------->>")
print("<<-------------------------------------------------------->>")
print("Total 'HOT' token:", sum(total))
print(f"Total Hot wallet counted {count}/{len(js_usernames)}")
