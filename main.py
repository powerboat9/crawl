import HTMLParser from HTMLParser
import Thread from threading
import re
import request from urllib

def download(url):
    data = None
    req = request.Request(url)
    with request.urlopen(req) as freq: #File REQuest
        data = freq.read()
    return data

class Parse(HTMLParser):
    def __init__(self, url, saveList = (), unsafeList = (), hasParsedList = {}):
        self.saveList = saveList
        self.hasParsedList = hasParsedList
        self.unsafeList = unsafeList
        self.baseURL = url
        self.url = url
        super(Parse, self).__init__()
        self.getData = download(url)
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

def threadMethod(url, saveList, hasParsedList):
    v = UnderstandURL(url)
    if v.isOK():
        