# Data Science Course

This repository accompanies my Data Science course. It currently contains a small Python web-scraping exercise and its saved text output. This README also records the main ideas and takeaways from the introductory Week 1 material.

## About the course

Data science brings together statistics, computing, algorithms, and knowledge of a subject area to turn data into useful evidence. The work goes beyond running an analysis: it includes choosing a question, collecting and understanding data, preparing it carefully, applying suitable methods, and communicating what the results do and do not show.

The introductory material covers:

- **Why data work is challenging at scale:** the volume, velocity, and variety of modern data.
- **How data is represented:** structured, semi-structured, and unstructured data, including CSV, TSV, XML, and JSON.
- **How to prepare data:** identifying missing, noisy, and inconsistent values; integrating sources; and checking for conflicts or duplication.
- **How data can be transformed:** smoothing, aggregation, generalization, scaling (normalization), and creating features.
- **How to simplify data when appropriate:** data-cube aggregation, dimensionality reduction, and discretization.

This summary reflects the introductory Week 1 material currently available to me; it is not a complete syllabus for the course.

## What I take from the course

I am learning to treat data analysis as a careful, end-to-end process. In practice, that means:

1. Start with a clear question and understand where the data came from.
2. Check what each row, field, unit, and value means before analyzing it.
3. Investigate data-quality issues instead of changing or removing values automatically.
4. Combine and transform data in ways that fit the question, while recording assumptions and preserving useful detail.
5. Use statistical reasoning, computing, and subject knowledge together, then explain conclusions with their limits.

## Current exercise: web scraper

`web-scraper.py` requests a web page, extracts its title and paragraph text, prints the results, and saves them to `text.txt`. If no URL is supplied, it uses `https://github.com/guuly05`.

Install the Python dependencies with:

```bash
python -m pip install requests beautifulsoup4
```

Run it with an optional page URL:

```bash
python web-scraper.py [URL]
```

The script currently writes to a local path configured inside the file, so update that path if you run it from a different machine or folder.
