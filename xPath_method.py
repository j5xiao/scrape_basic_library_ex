import logging
import re
from urllib.parse import urljoin

from url_file import url_get, default_url

URL = default_url()

from lxml import etree

"""
example
"""

# text = """
# <div class="container">
#         <h2>My Favorite Movies</h2>
#         <ul class="movie-list">
#             <li data-id="1">The Shawshank Redemption</li>
#             <li data-id="2">The Godfather</li>
#             <li data-id="3">The Dark Knight</li>
#             <li data-id="4">Pulp Fiction</li>
#             <li data-id="5">Forrest Gump</li>
#         </ul>
#     </div>
# """

# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

from requests_method import scrape_page

def read_url_index(url, page_number=1):
    url_index = f'{url}/page/{page_number}'
    return scrape_page(url_index)

def get_index(html):
    html = etree.HTML(html)
    index_lst = html.xpath('//div/div/div/a[@class="name"]/@href')
    if index_lst == []:
        return []
    for i in index_lst:
        yield urljoin(URL, i)

def get_name(html):
    html = etree.HTML(html)
    name = html.xpath('//div/div/a/h2/text()')
    return name[0]
    


def main(url=URL, number=1):
    html = read_url_index(url, number)
    group_index = list(get_index(html))
    for i in group_index:
        html_content = scrape_page(i)
        print(get_name(html_content))

if __name__ == '__main__':
    main()


