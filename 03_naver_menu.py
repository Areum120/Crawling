import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

# print(bs_obj)

ul = bs_obj.find("ul", {"class":"list_nav type_fix"})

lis = ul.findAll("li")#대괄호로 여러줄을 하나로 즉, list로 출력됨
print(lis)


# for li in ul:
#     print(li)
