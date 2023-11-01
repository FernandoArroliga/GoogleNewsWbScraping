# Google News Web Scraper

This Python script enables scraping of Google News articles related to technology using Beautiful Soup.

**Author:** Fernando Arroliga  
**Created:** 2023-10-30  
**Version:** 1.0

## Overview

This script is designed to scrape technology-related news articles from Google News. It extracts both the article titles and their corresponding links and writes this information to a text file.

## Requirements

The script utilizes the following libraries:
- BeautifulSoup
- requests
- datetime

To install the necessary dependencies, you can use the following command:

```bash
  pip install beautifulsoup4 requests
```


## Usage

1. Clone or download the repository.
2. Run the Python script `google_news_scraper.py`.
3. The script will fetch and scrape the latest technology news from Google News.
4. The scraped headlines and their links will be saved to a text file named based on the current date.

## File Description

- `google_news_scraper.py`: Main Python script for scraping Google News.
- `DayOfWeek_Date.txt`: Output file containing the scraped article titles and links, named according to the day of scraping.

## Contribution

Contributions to improve and extend this web scraping script are welcome. Feel free to fork the repository and create a pull request with your proposed changes.

## License

This project is licensed under the [MIT License](LICENSE).
