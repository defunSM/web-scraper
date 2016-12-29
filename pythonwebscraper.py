#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

def main():

    link = 'https://en.wikipedia.org/wiki/Physics'
    resp = requests.get(link)
    soup = BeautifulSoup(resp.text, 'lxml')

    urls = []
    for h in soup.find_all('p'):

        a = h.find_all('a')

        for t in a:

            urls.append(t.attrs['href'])


    f = open('urls.txt', 'w')

    for url in urls:

        if '#' in url:
            pass
        else:
            f.write(link + url)
            f.write("\n")

    f.close()






if __name__=="__main__":
    main()
