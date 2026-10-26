import requests
from bs4 import BeautifulSoup
from pathlib import Path
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

tables = data.find_all("table")
if not tables:
    print("No tables found.")

filepath = Path(__file__).with_name("tables.txt")
with open(filepath, "w", encoding="utf-8") as f:
    if title:
        f.write(title.get_text(" ", strip=True) + "\n")

    for table_number, table in enumerate(tables, start=1):
        print(f"Table {table_number}")
        f.write(f"\nTable {table_number}\n")

        for row in table.find_all("tr"):
            cells = row.find_all(["th", "td"])
            values = [cell.get_text(" ", strip=True) for cell in cells]
            if any(values):
                line = "\t".join(values)
                print(line)
                f.write(line + "\n")

print(f"Saved tables to {filepath}")
