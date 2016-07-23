def download(url):
    data = None
    req = request.Request(url)
    with request.urlopen(req) as freq: #File REQuest
        data = freq.read()
    return data