import requests
from bs4 import BeautifulSoup
import re


def get_internal_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the main content area
    content = soup.find('div', {'id': 'bodyContent'})

    # Find all links in the content area that start with '/wiki/'
    internal_links = content.find_all('a', href=re.compile('^/wiki/'))

    # Extract and return the URLs
    urls = [link['href'] for link in internal_links]
    useful_links = []

    for num, link in enumerate(urls):
        if "/wiki/File:" in link:
            ...
        elif "/wiki/Category:" in link:
            ...
        elif "/wiki/Special:" in link:
            ...
        elif "/wiki/Template:" in link:
            ...
        elif "/wiki/Wikipedia:" in link:
            ...
        elif "/wiki/Help:" in link:
            ...
        elif "/wiki/Template_talk:" in link:
            ...
        else:
            useful_links.append(link)


    return ['https://en.wikipedia.org' + link for link in useful_links]


