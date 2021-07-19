import requests
from bs4 import BeautifulSoup

# 네이버 금융 첫페이지 받아오기
def get_bs_obj():
    url = "https://finance.naver.com/item/main.nhn?code=005930"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# bs_obj를 받아서 price를 return하게
def get_price(bs_obj):
    no_today = bs_obj.find("p", {"class":"no_today"})
    blind_now = no_today.find("span",{"class":"blind"})
    return blind_now.text

bs_obj = get_bs_obj()
price = get_price(bs_obj)
print(price)