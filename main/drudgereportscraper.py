import basicscraper

class Drudgereportscraper(basicscraper.Scraper):
    def __init__(self):
        url = 'https://www.drudgereport.com'
        blacklist_file = 'drudgereportblacklist.txt' 
        headlines_file = 'drudgereport_headlines.txt'
        super().__init__(url, blacklist_file, headlines_file)

    def extract_headlines(self, soup):
        return soup.find_all('a')