from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import requests

import pdb

# URL = 'https://www.sec.gov/edgar/browse/'
URL = 'https://www.sec.gov/edgar/browse/?CIK=1652044&owner=exclude'
# "https://www.sec.gov/edgar/searchedgar/companysearch.html"

# Name and CIK pairs
COMPANIES = {
    'EA': '0000712515',
    'airbnb': '0001559720', 
    'Alphabet':'0001652044'
}




def main():
    # with open('html.txt', 'w') as f:
    #     r = requests.get(URL)
    #     print(1)
    #     s = BeautifulSoup(r.content, 'html.parser')
    #     print(2)
    #     x = s.find_all('div', {'id': 'filings'})
    #     print(x, file=f)
    #     print(3)

    chrome_options = Options()
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--no-sandbox") # linux only
    # chrome_options.add_argument("--headless")
    # chrome_options.headless = True # also works
    driver = webdriver.Chrome(options=chrome_options)
    service_object = Service(binary_path)
    driver = webdriver.Chrome(service=service_object, options=chrome_options)
    # driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()

    # deprecated but works in older selenium versions
    # driver = webdriver.Chrome(executable_path=binary_path)
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//*[@id="filingsStart"]/div[2]/div[3]/h5')
    element.click()
    pdb.set_trace()
    element = driver.find_element(By.XPATH, '//*[@id="filingsStart"]/div[2]/div[3]/div/button[1]')
    element.click()
    pdb.set_trace()
    elements = driver.find_elements(By.CSS_SELECTOR, 'a.document-link')
    print(len(elements))
    pdb.set_trace()
    elements = driver.find_elements(By.TAG_NAME, 'tr')
    print(len(elements))
    pdb.set_trace()
    print("Hello World!")
    # //*[@id="filingsTable"]/tbody/tr[1]/td[2]/div/a[1]
    # //*[@id="filingsTable"]/tbody/tr[2]/td[2]/div/a[1]

    # Open 10-K and 10-Q collapsible
    # Open all filings
    # Open desired filings
    # Extract desired components
    # Store sequentially with date as headers


if __name__ == "__main__":
    main()
