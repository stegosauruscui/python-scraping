from urllib.request import urlopen
#Retrieve HTML string from the URL
"""
如果你用过 Python 2.x 里的 urllib2 库，可能会发现 urllib2 与 urllib 有些不同。
在 Python 3.x 里， urllib2 改名为 urllib， 被分成一些子模块： urllib.request 、 urllib.parse 和 urllib.error 。
尽管函数名称大多和原来一样，但是在用新 的 urllib 库时需要注意哪些函数被移动到子模块里了。
"""
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
print(html.read())