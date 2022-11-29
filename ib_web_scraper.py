from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path

from bs4 import BeautifulSoup
import requests

import pdb
import sys

# URL = 'https://www.sec.gov/edgar/browse/'
URL = 'https://www.sec.gov/edgar/browse/?CIK=1652044&owner=exclude'
# "https://www.sec.gov/edgar/searchedgar/companysearch.html"

# Name and CIK pairs
COMPANIES = {
    'EA': '0000712515',
    'airbnb': '0001559720', 
    'Alphabet':'0001652044'
}

class element:
    def __init__(self, driver, loc_strat, loc):
        self.driver = driver
        self.loc_strat = loc_strat,
        self.loc = loc

        if self.loc_strat == 'id':
            self.element = (By.ID, self.loc)
        elif self.loc_strat == 'name':
            self.element = (By.NAME, self.loc)
        elif self.loc_strat == 'xpath':
            self.element = (By.XPATH, self.loc)
        elif self.loc_strat == 'link_text':
            self.element = (By.LINK_TEXT, self.loc)
        elif self.loc_strat == 'partial_link_text':
            self.element = (By.PARTIAL_LINK_TEXT, self.loc)
        elif self.loc_strat == 'tag_name':
            self.element = (By.TAG_NAME, self.loc)
        elif self.loc_strat == 'class_name':
            self.element = (By.CLASS_NAME, self.loc)
        elif self.loc_strat == 'css_selector':
            self.element = (By.CSS_SELECTOR, self.loc)
        else:
            sys.exit('Invalid element paramters: {self.loc_strat}, {self.loc}')

    def __str__(self):
        return f'Element: {self.loc_strat}, {self.loc}'

    def click(self, wait=0):
        try:
            clickable = WebDriverWait(self.driver, wait).until(
                    EC.element_to_be_clickable(self.element)
                )
            clickable.click()
        finally:
            sys.exit(f'{self.element} not clickable')


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
    service_object = Service(binary_path)
    driver = webdriver.Chrome(service=service_object, options=chrome_options)
    driver.implicitly_wait(10)
    # driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()

    # deprecated but works in older selenium versions
    # driver = webdriver.Chrome(executable_path=binary_path)
    driver.get(URL)
    html_source_code = driver.execute_script("return document.body.innerHTML;")
    html_soup = BeautifulSoup(html_source_code, 'html.parser').prettify()
    with open('html.txt', 'w') as f:
        print(html_soup, file=f)
    pdb.set_trace()
    element = driver.find_element(By.XPATH, '//*[@id="filingsStart"]/div[2]/div[3]/h5')
    element.click()
    # pdb.set_trace()
    element = driver.find_element(By.XPATH, '//*[@id="filingsStart"]/div[2]/div[3]/div/button[1]')
    element.click()
    # pdb.set_trace()
    elements = driver.find_elements(By.CSS_SELECTOR, 'a.document-link')
    # print(len(elements))
    # pdb.set_trace()
    elements = driver.find_elements(By.TAG_NAME, 'tr')
    # print(len(elements))
    pdb.set_trace()
    with open('html2.txt', 'w') as f:
        print(driver.page_source.prettify(), file=f)
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
