import basicscraper

class Foxnewsscraper(basicscraper.Scraper):
    def __init__(self):
        url = 'https://www.foxnews.com'
        blacklist_file = 'foxnewsblacklist.txt' 
        headlines_file = 'foxnews_headlines.txt'
        super().__init__(url, blacklist_file, headlines_file)

    def extract_headlines(self, soup):
        return soup.find_all('h3', {'class': 'title'})