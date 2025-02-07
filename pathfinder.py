#there is a function named linkcollektor, 
# input url
# output list of urls
# aim is to find a path from input to output url from wikipedia

#import the Linkcollector function from LinlCollector.py
from LinkCollecter import get_internal_links


def find_path(start_url, end_url):
    visited = set()
    queue = [(start_url, [start_url])]

    while queue:
        current_url, path = queue.pop(0)
        if current_url == end_url:
            return path
        if current_url not in visited:
            visited.add(current_url)
            for link in get_internal_links(current_url):
                if link not in visited:
                    queue.append((link, path + [link]))
    
if __name__ == "__main__":
    start_url = "https://en.wikipedia.org/wiki/Web_scraping"
    end_url = "https://en.wikipedia.org/wiki/Blacksburg,_Virginia"
    path = find_path(start_url, end_url)
    if path:
        print("Path found:")
        for url in path:
            print(url)
    else:
        print("No path found.")

