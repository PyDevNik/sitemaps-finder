from csv_reader import load
from csv_saver import save
from sitemap_parser import parse_sitemap

import threading 

print("Sitemap loader | Visit result.csv")

data = load("links.csv", "link")

def thread(url):
    sitemap = parse_sitemap(url)
    urls.append(sitemap)
    result = save("result.csv", "link", urls)

urls = []

for url in data:
   threading.Thread(target = thread, args = (url,)).start()
