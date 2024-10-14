import requests
from bs4 import BeautifulSoup
from typing import List
from global_webscraper.scraper.utilities import extract_url_webpage, validate_url_webpage, extract_chunks
import functools
import operator

class WebScraper:
    @staticmethod
    def scrap_website(base_url: str, max_extra_webpages: int = 0) -> List[str]:
        """Scrap website with all on a tag on the page"""
        page = f"{base_url}"        
        request = requests.get(page)
        soup = BeautifulSoup(request.text, "html.parser")
        
        urls = validate_url_webpage(extract_url_webpage(soup), base_url)[:max_extra_webpages]
        
        urls.append(base_url)
        
        chunks = [extract_chunks(BeautifulSoup(requests.get(url).text, "html.parser")) for url in urls]

        chunks = functools.reduce(operator.iconcat, chunks, [])
        
        return chunks