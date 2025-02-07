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
    urls = ['https://en.wikipedia.org' + link['href'] for link in internal_links]
    useful_links = []

    for num, link in enumerate(urls):
        if "https://en.wikipedia.org/wiki/File:" in link:
            ...
        elif "https://en.wikipedia.org/wiki/Category:" in link:
            ...
        else:
            useful_links.append(link)

    return useful_links

# Example usage
wikipedia_url = "https://en.wikipedia.org/wiki/Congress_of_Jalisco"
internal_urls = get_internal_links(wikipedia_url)

for url in internal_urls:
    print(url)
