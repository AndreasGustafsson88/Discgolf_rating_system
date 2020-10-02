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


def course_stats(name):
    dict1 = defaultdict(list)

    with open(f"{PLAYER_PATH}\\{name}.csv", "r", encoding="utf-8") as score_card:
        index = 0
        for h, i in enumerate(csv.reader(score_card)):
            if "Par" in i[0]:
                for j in range(24):
                    dict1[i[1]].append({j+1: [i[j + 6], []]})
                                 # [i[6], []], [i[7], []], [i[8], []], [i[9], []], [i[10], []], [i[11], []], [i[12], []],
                                 # [i[13], []], [i[14], []], [i[15], []], [i[16], []], [i[17], []], [i[18], []],
                                 # [i[19], []], [i[20], []], [i[21], []], [i[22], []], [i[23], []],
                                 # ])
            if name.lower() in i[0].lower():
                dict1[index][0].append(i[4])
                for count in range(1, 25):
                    try:
                        dict1[index][count][1].append(i[count + 5])
                    except IndexError:
                        continue
                index += 1
    return dict1
