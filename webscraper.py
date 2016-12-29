#!/usr/bin/env python
import sys, os
import requests

from lxml import html
from os.path import basename
from urllib.parse import urljoin
from lxml import etree

import scraperwiki
import lxml.html

def example():

    response = requests.get("https://en.wikipedia.org/robots.txt")
    txt = response.text

    print(txt)

def geolocation():

    base_url = 'http://maps.googleapis.com/maps/api/geocode/json'
    my_params = {'address': '100 Broadway, New York, NY, U.S.A',
                 'language': 'ca'}
    response = requests.get(base_url, params = my_params)
    results = response.json()['results']
    x_geo = results[0]['geometry']['location']
    print(x_geo['lng'], x_geo['lat'])

def textcontent():

    page = requests.get("https://en.wikipedia.org/wiki/Physics").text
    doc = html.fromstring(page)
    link = doc.cssselect("a")[0]
    print(link.text_content())
    print(link.attrib['href'])

def testscores():

    base_url = 'http://www.cde.ca.gov/ds/sp/ai/'
    page = requests.get(base_url).text
    doc = html.fromstring(page)
    hrefs = [a.attrib['href'] for a in doc.cssselect('a')]
    xls_hrefs = [href for href in hrefs if 'xls' in href]

    for href in xls_hrefs:
        print(href) # e.g. documents/sat02.xls
        url = urljoin(base_url, href)

        with open("/tmp/" + basename(url), 'wb') as f:
            print("Downloading", url)
            # Downloading http://www.cde.ca.gov/ds/sp/ai/documents/sat02.xls
            data = requests.get(url).content
            f.write(data)


def tut():

    base_url = "http://lxml.de/tutorial.html"
    page = requests.get(base_url).text

    html = etree.Element("html")
    body = etree.SubElement(html, "body")

    body.text = "TEXT"

    root = etree.fromstring(page)

    print(root.tag)

def scrap():

    html = scraperwiki.scrape('https://defunsm.github.com')

    root = lxml.html.fromstring(html)
    # get the links
    hrefs = root.xpath('//td[@class="mys-elastic mys-left"]/a')

    for href in hrefs:
        print('https://defunsm.github.com' + href.attrib['href'])


def main():
    scrap()

if __name__=="__main__":
    main()
