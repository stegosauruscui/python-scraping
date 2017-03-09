from urllib.request import urlopen
from bs4 import BeautifulSoup

"""
通过

BeautifulSoup

对象，我们可以用 findAll 函数抽取只包含在 <span class="green"></ span> 标签里的文字，
这样就会得到一个人物名称的 Python 列表（ findAll 是一个非常灵 活的函数，我们后面会经常用到它）
"""


html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())