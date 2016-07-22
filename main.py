import HTMLParser from HTMLParser
import Thread from threading

class Save(HTMLParser):
    def handle_starttag():
        

def parse(self, saveList, url, hasParsedReg):
    if url[:1] == "//":
        url = "https://"
    if url[:7] != "https://" && url[:6] != "http://":
        raise Exception("Could not search invalid URI scheme")
    self.
