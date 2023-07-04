import requests
import os
from bs4 import BeautifulSoup
from datetime import date

class Scraper:
    def __init__(self, url, blacklist_file, headlines_file):
        self.url = url
        self.blacklist_file = blacklist_file
        self.headlines_file = headlines_file

    def scrape_data(self):
        excluded_lines = self.read_excluded_lines()

        response = self.send_get_request()
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            headlines = self.extract_headlines(soup)

            headline_list = []
            for headline in headlines:
                headline_text = headline.text.strip()
                if headline_text and headline_text not in excluded_lines:
                    headline_list.append(headline_text)

            self.save_headlines(headline_list)
            print("Headlines saved to", self.headlines_file)
        else:
            print(f"Error: {response.status_code}")

    def read_excluded_lines(self):
        with open(os.path.join('blacklists', self.blacklist_file), 'r') as blacklist_file:
            return [line.strip() for line in blacklist_file.readlines()]

    def send_get_request(self):
        return requests.get(self.url)

    def extract_headlines(self, soup):
        raise NotImplementedError("Subclasses must implement the extract_headlines method.")

    def save_headlines(self, headline_list):
        current_date = date.today().strftime("%Y-%m-%d")
        subfolder_name = os.path.join('headlines', current_date)
        os.makedirs(subfolder_name, exist_ok=True)  # Create the subfolder if it doesn't exist
        filename = current_date + "_" + self.headlines_file
        self.headlines_file = os.path.join(subfolder_name, filename)

        with open(self.headlines_file, 'w', encoding='utf-8') as file:
            for headline in headline_list:
                file.write(f"{headline}\n")




