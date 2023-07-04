import os
import importlib

def main():
    scraper_files = [filename for filename in os.listdir() if filename.endswith('scraper.py') and filename != 'basicscraper.py']

    for scraper_file in scraper_files:
        module_name = os.path.splitext(scraper_file)[0]
        module = importlib.import_module(module_name)
        scraper_class = getattr(module, module_name.capitalize())
        scraper = scraper_class()
        scraper.scrape_data()

if __name__ == '__main__':
    main()