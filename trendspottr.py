import html2text
import os
import requests
from urllib import parse


def get_trending(topic_string):
    base_url = 'https://api.trendspottr.com/v1.5/search?'
    base_url += 'key=' + os.environ.get('TS_KEY') + '&'
    base_url += 'q=' + parse.quote(topic_string) + '&'
    base_url += 'w=all&'
    base_url += 'resolve_urls=true&'
    base_url += 'expand=true'
    response = requests.get(base_url)
    json = response.json()
    links = json["results"]["links"]
    return links[0]["expanded"]["url"]


def retrieve_text_from(link):
    response = requests.get(link)
    html = response.text
    html_converter = html2text.HTML2Text()
    html_converter.ignore_links = True
    text = html_converter.handle(html)
    return text
