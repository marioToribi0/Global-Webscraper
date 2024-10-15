from scraper.model import WebScraper
from embedding.embedded import get_embedding

if __name__ == "__main__":
    chunks = WebScraper.scrap_website("https://www.unibe.edu.do")[:4]
    
    chunks = [{"content": chunk, "vector": get_embedding(chunk)} for chunk in chunks]
    
    print(chunks)
    