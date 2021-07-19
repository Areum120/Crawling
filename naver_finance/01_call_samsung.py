import requests
from bs4 import BeautifulSoup

# 네이버 금융 첫페이지 받아오기
def get_bs_obj():
    url = "https://finance.naver.com/item/main.nhn?code=005930"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj
    print(bs_obj)
    # print(result.content)

bs_obj = get_bs_obj()
print(bs_obj)

#