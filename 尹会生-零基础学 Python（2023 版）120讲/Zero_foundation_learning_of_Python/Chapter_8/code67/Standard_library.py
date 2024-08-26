from urllib.request import urlopen

with urlopen("https://www.baidu.com/") as url:
    print(url.read(300))
