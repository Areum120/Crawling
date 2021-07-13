import bs4
html_str = "<html><div></div></html>"
bs0bj = bs4.BeautifulSoup(html_str, "html.parser")
print(bs0bj)
print(type(bs0bj))
print(bs0bj.find("div"))