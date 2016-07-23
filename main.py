import HTMLParser from HTMLParser
import Thread from threading
import re

class Parse(HTMLParser):
    def __init__(self, url, saveList = (), unsafeList = (), hasParsedList = {}):
        self.saveList = saveList
        self.hasParsedList = hasParsedList
        self.unsafeList = unsafeList
        self.baseURL = url
        self.url = url
        super(Parse, self).__init__()
    def unsafe(self, url):
        if !self.hasParsedList[url]:
            self.unsafeList[self.unsafeList.length] = url
            self.hasParsedList[url]
    def share(self, url):
        if !self.hasParsedList[url]:
            self.saveList[self.saveList.length] = url
            self.hasParsedList[url] = True
            return True
        return False
    def create(self, link):
        if self.share(link):
            newThread = Thread(target = threadMethod, args = (link, self.saveList, self.hasParsedList))
            newThread.daemon = True
            newThread.start()
    def handle_starttag(self, tag, attributes):
        if tag == "a" || tag == "link":
            self.create(attributes.href)
        elif tag == "script" || tag == "img" || tag == "audio" || tag == "embed":
            self.share(attributes.src)
        elif tag == "iframe" || tag == "source":
            self.create(attributes.src)
        elif tag == "object":
            self.create()
        elif tag == "form":
            self.unsafe(attributes.action)

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
