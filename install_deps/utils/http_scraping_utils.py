"""HTTP client / scraping dependencies.

One function per dependency: requests, httpx, aiohttp, beautifulsoup4 (bs4),
lxml, scrapy, selenium.
"""

import requests
import httpx
import aiohttp
from bs4 import BeautifulSoup
import lxml.etree as etree
import scrapy
from selenium import webdriver


def fetch_url(url: str) -> str:
    """requests: GET a URL and return the response text."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def httpx_get(url: str) -> int:
    """httpx: GET a URL and return the status code."""
    response = httpx.get(url, timeout=10)
    return response.status_code


async def aiohttp_get(url: str) -> str:
    """aiohttp: asynchronously GET a URL and return its text."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def parse_links(html: str) -> list[str]:
    """beautifulsoup4: extract all link hrefs from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    return [a["href"] for a in soup.find_all("a", href=True)]


def parse_xml_tags(xml: str) -> list[str]:
    """lxml: parse XML and return the tag names of the root's children."""
    root = etree.fromstring(xml.encode())
    return [child.tag for child in root]


def css_select(html: str, query: str = "a::attr(href)") -> list[str]:
    """scrapy: use a Scrapy Selector to run a CSS query over HTML."""
    selector = scrapy.Selector(text=html)
    return selector.css(query).getall()


def build_chrome_options():
    """selenium: build a headless Chrome options object (no driver launch)."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    return options
