import requests
from bs4 import BeautifulSoup

class WebScraper:
    pass

if __name__ == "__main__":
    page = f"https://www.unibe.edu.do"
    
    request = requests.get(page)
    soup = BeautifulSoup(request.text, "html.parser")
    
    print(soup.text)