import requests
from urllib import parse 

def parse_sitemap(url):
    try:
        data = parse.urlparse(url)
        scheme = data.scheme
        loc = data.netloc
        url = scheme + "://" + loc
        robots_url = parse.urljoin(url, '/robots.txt')
        response = requests.get(robots_url)
        robots = response.text
        sitemap_url = ""

        for line in robots.split('\n'):
            if line.lower().startswith('sitemap: '):
                sitemap_url = line.split(': ')[1].strip()
                if not sitemap_url.startswith(url):
                    sitemap_url = parse.urljoin(url, sitemap_url)
                break

        if not sitemap_url:
            for i in ["sitemap", "/sitemap.xml", "sitemap_index.xml"]:
                sitemap_url = parse.urljoin(url, i)
                response = requests.get(sitemap_url)
                if response.status_code == 200:
                    break
        response.raise_for_status()
        return sitemap_url
        
    except:
        return ""
