from urllib.request import urlopen
html = urlopen("http://127.0.0.1/files/")
print(html.read())