import basicscraper

class Bbcscraper(basicscraper.Scraper):
    def __init__(self):
        url = 'https://www.bbc.com'
        blacklist_file = 'bbcblacklist.txt' 
        headlines_file = 'bbc_headlines.txt'
        super().__init__(url, blacklist_file, headlines_file)

    def extract_headlines(self, soup):
        return soup.find_all('h3')