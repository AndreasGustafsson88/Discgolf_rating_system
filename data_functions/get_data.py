import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
from collections import defaultdict


DRIVER_PATH = "C:\Program Files (x86)\Webdrivers\chromedriver.exe"
PLAYER_PATH = "C:\Kod\Projekt\Handicap system for Discgolf\Player_data"


def download(event_link, element_class="table-container",  headless=True):
    options = Options()
    options.headless = headless
    options.add_argument("--window-size=2000,1200")

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(event_link)
    return [rating.text for rating in driver.find_elements_by_class_name(element_class)]


def read_csv(name):
    dict1 = defaultdict(list)
    with open(f"{PLAYER_PATH}\\{name}.csv") as score_card:
        for i in csv.reader(score_card):
            if name in i[0]:
                dict1[i[1]].append(int(i[4]))
    return {key: dict1[key] for key in sorted(dict1)}


def calculate_rating():
    pass


