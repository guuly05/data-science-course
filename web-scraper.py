import requests
from bs4 import BeautifulSoup
import sys

url = sys.argv[1] if len(sys.argv) > 1 else "https://github.com/guuly05"

try:
    page = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; SimpleScraper/1.0)"},
        timeout=15,
    )
    page.raise_for_status()
except requests.RequestException as error:
    print(f"Could not fetch {url}: {error}")
    raise SystemExit(1)

data = BeautifulSoup(page.text, "html.parser")

title = data.find("h1") or data.find("title")
print(title.get_text(" ", strip=True) if title else "No title found")

article = data.find("div", class_="main-article") or data
paragraphs = article.find_all("p")
if not paragraphs:
    print("No paragraphs found.")

for paragraph in paragraphs:
    text = paragraph.get_text(" ", strip=True)
    if text:
        print(text)

filepath = r"C:\Users\THINKPAD\Music\mobile application development\data science\text.txt"
with open(filepath, "w", encoding="utf-8") as f:
    if title:
        f.write(title.get_text(" ", strip=True) + "\n")
    for paragraph in paragraphs:
        text = paragraph.get_text(" ", strip=True)
        if text:
            f.write(text + "\n")