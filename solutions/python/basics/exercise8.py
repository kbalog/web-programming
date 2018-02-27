"""
Write a function to parse a website's title (e.g., [this](http://www.pythonscraping.com/pages/page1.html)).
Use try-except to capture the exceptions like the web can not be opened or the title does not exist.
It is recommended that you make use of existing packages (BeautifulSoup or urllib.request) in this exercise.
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.title
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found!")
else:
    print(title)
