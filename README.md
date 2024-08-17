# Web Scraping Project

This project demonstrates how to scrape data from a webpage using Python. The script fetches country data from a sample website and writes the data to a CSV file.

## Features

- Fetches HTML content from a webpage
- Parses HTML content using BeautifulSoup
- Extracts country names, capitals, populations, and areas
- Stores the extracted data in a CSV file

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/navarronet/web-scraping-project.git
    cd web-scraping-project
    ```

2. Install the required libraries:
    ```sh
    pip install requests beautifulsoup4
    ```

## Usage

1. Run the script:
    ```sh
    python webScraping.py
    ```

2. The script will fetch data from the webpage and save it to `countries.csv`.

## Code Overview

- `webScraping.py`: Main script that performs web scraping and writes data to a CSV file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
