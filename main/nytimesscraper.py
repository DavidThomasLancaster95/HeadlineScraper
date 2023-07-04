import basicscraper

class Nytimesscraper(basicscraper.Scraper):
    def __init__(self):
        url = 'https://www.nytimes.com'
        blacklist_file = 'nytimesblacklist.txt' 
        headlines_file = 'nytimes_headlines.txt'
        super().__init__(url, blacklist_file, headlines_file)

    def extract_headlines(self, soup):
        return soup.find_all('h3')