import basicscraper

class Nypostscraper(basicscraper.Scraper):
    def __init__(self):
        url = 'https://www.nypost.com'
        blacklist_file = 'nypostblacklist.txt' 
        headlines_file = 'nypost_headlines.txt'
        super().__init__(url, blacklist_file, headlines_file)

    def extract_headlines(self, soup):
        return soup.find_all('h3')

