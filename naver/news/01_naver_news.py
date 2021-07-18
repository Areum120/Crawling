from urllib.request import urlopen
import bs4
import requests

url = "https://news.naver.com"

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" }
# 오류 : 무분별한 크롤링을 막기 위해 requests header의 user-agent 값이 문제
r = requests.get(url, headers=headers)
# print(r.text)

# html = urlopen(url)

bsObj = bs4.BeautifulSoup(r.text, 'html.parser')

# print(bsObj)

ul = bsObj.find("ul", {"class": "hdline_article_list"})
lis = ul.findAll("li")
# print(lis)

# for li in lis:
#     a_text = li.find("a")
#     print(a_text.text.strip())

titles = [li.find("a").text.strip() for li in lis]
# print(titles)
for title in titles:
    print("오늘의 기사는:", title)
