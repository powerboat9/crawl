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
    def isOK(self):
        return (self.URI == "https") || (self.URI == "http")
    def getDomain(self):
        return self.URI + "://" + self.domain