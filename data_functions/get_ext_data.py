from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
from collections import defaultdict

DRIVER_PATH = "C:\Program Files (x86)\Webdrivers\chromedriver.exe"
PLAYER_PATH = "C:\Kod\Projekt\Handicap system for Discgolf\Player_data"


def download(event_link, element_class="table-container", headless=True):
    options = Options()
    options.headless = headless
    options.add_argument("--window-size=2000,1200")

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(event_link)
    return [rating.text for rating in driver.find_elements_by_class_name(element_class)]


def read_csv(name):
    dict1 = defaultdict(list)

    with open(f"{PLAYER_PATH}\\{name}.csv", "r", encoding="utf-8") as score_card:
        for i in csv.reader(score_card):
            if name.lower() in i[0].lower():
                dict1[i[1]].append(int(i[4]))
    return {key: dict1[key] for key in sorted(dict1)}


def sort_rounds(name):
    with open(f"{PLAYER_PATH}\\{name}.csv", "r", encoding="utf-8") as score_card:
        return [[i[1], i[3], int(i[4])] for i in csv.reader(score_card) if name.lower() in i[0].lower()]


def course_stats(name): # WORK IN PROGRESS
    dict2 = defaultdict(dict)
    with open(f"{PLAYER_PATH}\\{name}.csv", "r", encoding="utf-8") as score_card:
        for h, i in enumerate(csv.reader(score_card)):
            if "Par" in i[0]:
                if dict2[i[1]] == {}:
                    try:
                        dict2[i[1]]["PAR"] = [int(i[4])]
                        for j in range(1, 19):
                            dict2[i[1]][j] = [int(i[j+5]) if i[j+5].isnumeric() else 0, []]
                    except IndexError:
                        continue
            if name.lower() in i[0].lower():
                try:
                    for j in range(1, 19):
                        if i[j+5].isnumeric():
                            dict2[i[1]][j][1].append(int(i[j+5]))
                except KeyError:
                    continue
    print(dict2)
    return dict2

