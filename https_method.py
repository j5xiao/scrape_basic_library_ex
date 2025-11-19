import httpx
import requests
import logging
import re
from urllib.parse import urljoin

from url_file import url_get

### get url by yourself
# URL = url_get()
URL = 'https://ssr1.scrape.center/'

# response = httpx.get(URL)
# print(response.status_code)
# print(response.text)

def scrape_page(url):
    try:
        respones = httpx.get(url)
        if respones.status_code == 200:
            return respones.text
    except:
        print("Wrong!")

def url_page(url, page):
    url_path = f'{url}page/{page}'
    return scrape_page(url_path)

def parse_index(html):
    re_index = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(re_index, html)
    if not items:
        return []
    for i in items:
        detail_url = urljoin(URL, i)
        yield detail_url

def scrape_content(url):
    html = scrape_page(url)
    re_name = re.compile('<h2.*?>(.*?)</h2>')
    name = re.search(re_name, html).group(1).strip() if re.search(re_name, html) else None
    return name

def main():
    menu_content = url_page(URL, 1)
    content_url = parse_index(menu_content)
    for i in list(content_url):
        print(scrape_content(i))

if __name__ == '__main__':
    main()

