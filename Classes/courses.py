from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Classes.cleaning_data import CleaningData

import matplotlib.pyplot as plt
import numpy as np

from data_functions import handle_data
from data_functions.get_data import download
from data_functions.graph_rating_score import plot_data
from data_functions.handle_data import convert_ratings_to_dict

DRIVER_PATH = "C:\Program Files (x86)\Webdrivers\chromedriver.exe"


class Course:
    def __init__(self, name, location, event_link, num_holes=18):
        self.name = name
        self.location = location
        self.num_holes = num_holes
        self.event_link = event_link
        self.raw_data = download("https://www.pdga.com/tour/event/46819")
        self.clean_data = handle_data.convert_to_int(handle_data.clean_raw_data(self.raw_data))
        self.latest_scores, self.latest_rating = handle_data.split_list(self.clean_data)
        self.rating = self.calculate_rating()

    # Make latest_score & latest_rating iterable
    def __str__(self):
        for i in range(len(self.latest_rating)):
            print(f"{self.latest_scores[i]} {self.latest_rating[i]}")

    def plot_data(self):
        plot_data(self.latest_rating, self.latest_scores, self.name)

    def calculate_rating(self):
        return convert_ratings_to_dict(self.latest_rating, self.latest_scores)

    def store_data(self):
        pass # pickle


def main():
    pass


if __name__ == "__main__":
    main()
