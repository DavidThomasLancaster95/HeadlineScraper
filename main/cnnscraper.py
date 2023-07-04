import basicscraper

class Cnnscraper(basicscraper.Scraper):
    def __init__(self):
        url = 'https://www.cnn.com'
        blacklist_file = 'cnnblacklist.txt' 
        headlines_file = 'cnn_headlines.txt'
        super().__init__(url, blacklist_file, headlines_file)

    def extract_headlines(self, soup):
        return soup.find_all('span', {'data-editable': 'headline'})