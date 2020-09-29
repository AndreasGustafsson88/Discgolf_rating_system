import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
DRIVER_PATH = "C:\Program Files (x86)\Webdrivers\chromedriver.exe"


def download(event_link, element_class="table-container",  headless=True):
    options = Options()
    options.headless = headless
    options.add_argument("--window-size=2000,1200")

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(event_link)
    return [rating.text for rating in driver.find_elements_by_class_name(element_class)]
