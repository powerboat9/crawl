import download from basicDownload

class ParseRobots():
    def __init__(self, domain, userAgent):
        if userAgent == None || !isinstance(userAgent, str):
            raise Exception("Invalid User Agent")
        rURL = domain + "/robots.txt"
        retDownload = download(rURL)
        if retDownload[0]:
            self.data = retDownload[1]
        else:
            self.data = ""
        self.userAgent = userAgent
        
        

class UnderstandURL():
    def __init__(self, url)
        if url[:1] == "//":
            url = "https:" + url
        self.pattern = re.match("([^:]+)://([^./][.]?){,}(/)?([^/]+/){,}([^.]*)([.])(.*)")
        self.URI = self.pattern.group(1)
        self.domain = ""
        i = 0
        ok = True
        while ok:
            v = self.pattern.group(2 + i)
            if v == None:
                ok = False
                break
            elif v == "/":
                i += 1
                break
            else:
                self.domain += v
            i += 1
        if i < 2:
            self.isDomainOk = False
        self.branchURL = ()
        last = False
        while ok:
            v = self.pattern.group(2 + i)
            if v == None:
                ok = False
                break
            if v == ".":
                i += 1
                break
            else:
                if v[-2:] != "/":
                    v = v[:-2]
                self.branchURL[self.branchURL.length] = v
        self.extension = self.pattern.group(2 + i)
    @property
    def okDomain(self):
        return self.URI && self.isDomainOk
    @property
    def okURI(self):
        return self.isOk && ((self.URI == "https") || (self.URI == "http"))
    @property
    def catDomain(self):
        return self.URI + "://" + self.domain
    def robots(self)