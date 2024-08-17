import requests
from bs4 import BeautifulSoup
import csv

# Fetch the content of a webpage
url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Get the list of countries
for country in soup.find_all('h3', class_='country-name'):
    country_name = country.get_text(strip=True)
    print(country_name)

# Get the details of each country
for country_info in soup.find_all('div', class_='country-info'):
    capital = country_info.find('span', class_='country-capital').get_text(strip=True)
    population = country_info.find('span', class_='country-population').get_text(strip=True)
    area = country_info.find('span', class_='country-area').get_text(strip=True)
    print(f"Capital: {capital}, Population: {population}, Area: {area}")

# Initialize a list to store the data
data = []

# Get the list of countries
country_names = [country.get_text(strip=True) for country in soup.find_all('h3', class_='country-name')]

# Get the details of each country
country_infos = soup.find_all('div', class_='country-info')

# Combine the country names and details
for i, country_info in enumerate(country_infos):
    capital = country_info.find('span', class_='country-capital').get_text(strip=True)
    population = country_info.find('span', class_='country-population').get_text(strip=True)
    area = country_info.find('span', class_='country-area').get_text(strip=True)
    data.append({
        'country_name': country_names[i],
        'capital': capital,
        'population': population,
        'area': area
    })

print(data)

# Write the data to a CSV file with UTF-8 encoding
with open('countries.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['country_name', 'capital', 'population', 'area']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)
