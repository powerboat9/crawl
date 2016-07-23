import HTMLParser from HTMLParser
import Thread from threading

class Parse(HTMLParser):
    def __init__(self, saveList, hasParsedList):
        self.saveList = saveList
        self.hasParsedList = hasParsedList
        super(Parse, self).__init__()
    def create(self, link):
        newThread = Thread(target = threadMethod, args = (link, self.saveList, self.hasParsedList))
        newthread
    def handle_starttag(self, tag, attributes):
        if tag == "a" || tag == "link":
            self.create(attributes.href)
        elif tag == "script" || tag == "img" || :
            self.create(attributes.src)

def threadMethod(url, saveList, hasParsedList):
    if url[:1] == "//":
        url = "https://"
    if url[:7] != "https://" && url[:6] != "http://":
        raise Exception("Could not search invalid URI scheme")
    Save
