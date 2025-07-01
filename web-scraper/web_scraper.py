
---

## web-scraper/web_scraper.py

```python
import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print("Top Hacker News Headlines:")
    for i, item in enumerate(soup.select('.storylink')[:10], 1):
        print(f"{i}. {item.get_text()}")

if __name__ == "__main__":
    main()
