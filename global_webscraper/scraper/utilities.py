from urllib.parse import urljoin, urlparse
from typing import List
import re
from bs4 import BeautifulSoup

def is_valid_url(url: str) -> str:
    """Check if the URL is valid"""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def extract_url_webpage(soup: BeautifulSoup) -> List[str]:
    """Extract all of url from the webpage"""
    urls = []
    for tag_a in soup.find_all("a", href=True):
        url = tag_a.get("href")
        if is_valid_url(url):
            urls.append(url)
    return urls

def extract_chunks(soup: BeautifulSoup, chunks: int = 300) -> List[str]:
    """Extract list of chunks from a page"""
    batches = []
    content = soup.text.split()
    for i in range(len(content)//chunks+1):
        batches.append(" ".join(content[i*chunks:(i+1)*chunks]))
    return batches

def validate_url_webpage(list_url: List[str], base_url: str) -> List[str]:
    """Extract all url valid from a specific webpage"""
    pages = list(filter(lambda url: re.search(rf"{base_url}.*", url), list_url))
    
    return list(set(pages))