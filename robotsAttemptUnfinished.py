class ParseRobots():
    def setAgent(self, userAgent):
        if userAgent == None || !isinstance(userAgent, str):
            raise Exception("Invalid User Agent")
        self.userAgent = userAgent
    def __init__(self, domain, userAgent):
        if userAgent:
            self.setAgent(userAgent)
        rURL = domain + "/robots.txt"
        retDownload = download(rURL)
        if retDownload[0]:
            self.data = retDownload[1]
        else:
            self.data = ""
        self.parse()
    def parse(self):
        sections = re.split("\n{2,}", self.data)
        for section in sections:
            mList = re.findall("^([^ :]*): ?([^ \n]*) ?$", section)
            for i in range(mList.length):
                m = mList[i]
                if i
                if i == 0: