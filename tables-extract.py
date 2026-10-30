import csv
import sys
from itertools import zip_longest
from pathlib import Path

import requests
from bs4 import BeautifulSoup


DEFAULT_URL = "https://github.com/guuly05"
DEFAULT_OUTPUT = Path(__file__).with_name("table.csv")


def extract_table(table) -> list[list[str]]:
    rows = []
    for row in table.find_all("tr"):
        cells = row.find_all(["th", "td"])
        values = [cell.get_text(" ", strip=True) for cell in cells]
        if any(values):
            rows.append(values)

    if not rows:
        return []

    width = max(len(row) for row in rows)
    return [
        [value for value, _ in zip_longest(row, range(width), fillvalue="")]
        for row in rows
    ]


def main() -> int:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    output = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT

    try:
        page = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; SimpleScraper/1.0)"},
            timeout=15,
        )
        page.raise_for_status()
    except requests.RequestException as error:
        print(f"Could not fetch {url}: {error}")
        return 1

    data = BeautifulSoup(page.text, "html.parser")
    tables = data.find_all("table")
    if not tables:
        print(f"No tables found at {url}.")
        return 1

    table_number = 1
    if len(sys.argv) > 3:
        try:
            table_number = int(sys.argv[3])
        except ValueError:
            print("Table number must be an integer.")
            return 1

    if not 1 <= table_number <= len(tables):
        print(f"Table number must be between 1 and {len(tables)}.")
        return 1

    rows = extract_table(tables[table_number - 1])
    if not rows:
        print(f"Table {table_number} is empty.")
        return 1

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as csv_file:
        csv.writer(csv_file).writerows(rows)

    print(f"Saved table {table_number} ({len(rows) - 1} data rows) to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
