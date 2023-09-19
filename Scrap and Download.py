from selenium import webdriver

def get_url(path, url):
    options = webdriver.ChromeOptions()
    options.binary_location = path  # Set the path to the Chrome executable

    # Specify any other options you need (e.g., headless mode)
    # options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # Rest of your code for web scraping
    driver.quit()

if __name__ == "__main__":
    path = input("Enter Path : ")  # Path to the Chrome executable
    url = input("Enter URL : ")    # URL to scrape

    result = get_url(path, url)
from selenium import webdriver

def get_url(path, url):
    options = webdriver.ChromeOptions()
    options.binary_location = path  # Set the path to the Chrome executable

    # Specify any other options you need (e.g., headless mode)
    # options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # Rest of your code for web scraping
    driver.quit()

if __name__ == "__main__":
    path = input("Enter Path : ")  # Path to the Chrome executable
    url = input("Enter URL : ")    # URL to scrape

    result = get_url(path, url)
