import HTMLParser from HTMLParser
import Thread from threading
import re

class Parse(HTMLParser):
    def __init__(self, url, saveList, hasParsedList):
        self.saveList = saveList
        self.hasParsedList = hasParsedList
        self.baseURL = url
        self.url = url
        super(Parse, self).__init__()
    def create(self, link):
        newThread = Thread(target = threadMethod, args = (link, self.saveList, self.hasParsedList))
        newthread
    def handle_starttag(self, tag, attributes):
        if tag == "a" || tag == "link":
            self.create(attributes.href)
        elif tag == "script" || tag == "img" || :
            self.create(attributes.src)

class UnderstandURL():
    def __init__(self, url)
        self.pattern = re.match("([^:]+)://[^.].?")

def threadMethod(url, saveList, hasParsedList):
    if url[:1] == "//":
        url = "https://"
    elif url[0] == "/":
        url = 
    if url[:7] != "https://" && url[:6] != "http://":
        raise Exception("Could not search invalid URI scheme")
    Save
