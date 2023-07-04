import basicscraper

class Googlenewsscraper(basicscraper.Scraper):
    def __init__(self):
        url = 'https://www.news.google.com'
        blacklist_file = 'googlenewsblacklist.txt' 
        headlines_file = 'googlenews_headlines.txt'
        super().__init__(url, blacklist_file, headlines_file)

    def extract_headlines(self, soup):
        return soup.find_all('h4')