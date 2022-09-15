import requests
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://www.sec.gov/edgar/browse/'
# 'https://www.sec.gov/edgar/browse/?CIK=1652044&owner=exclude'
# "https://www.sec.gov/edgar/searchedgar/companysearch.html"

# Name and CIK pairs
COMPANIES = {
    'EA': '0000712515',
    'airbnb': '0001559720', 
    'Alphabet':'0001652044'
}




def main():
    driver = webdriver.Firefox()
    driver.get(URL)
    element = driver.find_element(By.linkText(" 10-K \
                        (annual reports) and \
                        10-Q (quarterly reports)"))
    # element = driver.find_element_by_link_text(" 10-K \
    #                     (annual reports) and \
    #                     10-Q (quarterly reports)")
    element.click()
    # page = requests.get(URL)
    # soup = BeautifulSoup(page.content, "html.parser")
    # print(soup)
    print("Hello World!")
    # Open 10-K and 10-Q collapsible
    # Open all filings
    # Open desired filings
    # Extract desired components
    # Store sequentially with date as headers


if __name__ == "__main__":
    main()
