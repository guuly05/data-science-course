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

### Extracting a table to CSV

`tables-extract.py` downloads a page, extracts one HTML table, and saves it as
CSV. Rows with missing cells are padded so every CSV row has the same number
of columns.

```bash
python tables-extract.py [URL] [OUTPUT_CSV] [TABLE_NUMBER]
```

All arguments are optional. The default URL is the GitHub profile used by the
other exercise, the default output is `table.csv` beside the script, and the
default table number is `1`.

## using numpy to analyze data
### what is numpy?
Numpy is a library that helps us with data analysis, it is used to perform mathematical operations, it is also used to perform operations on arrays and matrices
in numpy-tutorial.py we learn how to use numpy to analyze data, we learn how to use numpy to perform mathematical operations, we also learn how to use numpy to perform operations on arrays and matrices, we also learn how to use numpy to perform operations on dataframes, we also learn how to use numpy to perform operations on series, we also learn how to use numpy to perform operations on lists, we also learn how to use numpy to perform operations on tuples, we also learn how to use numpy to perform operations on dictionaries, we also learn how to use numpy to perform operations on sets, we also learn how to use numpy to perform operations on strings, we also learn how to use numpy to perform operations on booleans, we also learn how to use numpy to perform operations on complex numbers, we also learn how to use numpy to perform operations on dates and times, we also learn how to use numpy to perform operations on files, we also learn how to use numpy to perform operations on images, we also learn how to use numpy to perform operations on audio files, we also learn how to use numpy to perform operations on video files, we also learn how to use numpy to perform operations on pdf files, we also learn how to use numpy to perform operations on excel files, we also learn how to use numpy to perform operations on word files, we also learn how to use numpy to perform operations on powerpoint files, we also learn how to use numpy to perform operations on html files.

### using numpy on a real dataset
In this section we will use numpy to analyze a real dataset, we will use the nyc_taxis dataset, we will use numpy to perform mathematical operations on the dataset, numpy has various methods that help us with data analysis these include:
    1. np.mean() - this method helps us to find the mean of a dataset
    2. np.sum() - this method helps us to find the sum of a dataset
    3. np.median() - this method helps us to find the median of a dataset
    4. np.std() - this method helps us to find the standard deviation of a dataset
    5. np.var() - this method helps us to find the variance of a dataset
    6. np.min() - this method helps us to find the minimum value of a dataset
    7. np.max() - this method helps us to find the maximum value of a dataset
    8. np.genfromtxt() - this method helps us to read data from a text file and store it in a numpy array
    9. np.where() - this method helps us to find the indices of a dataset that satisfy a certain condition
    10. np.sort() - this method helps us to sort the elements of a dataset in ascending order

all of these methods are used in impor.py to analyze the nyc_taxis dataset, we will use these methods to find the mean, sum, median, standard deviation, variance, minimum value, maximum value, and sort the elements of the dataset in ascending order.
