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
    def __init__(self, name, location, num_holes=18):
        self.name = name
        self.location = location
        self.num_holes = num_holes
        self.data = []
        self.latest_scores, self.latest_rating = [], []

    def get_data(self, link):
        print("Getting raw data")
        raw_data = download(link)
        clean_data = handle_data.clean_raw_data(raw_data)
        clean_data_int = handle_data.convert_to_int(clean_data)
        self.latest_scores, self.latest_rating = handle_data.split_list(clean_data_int)
        print("Data download complete!")

    # Make latest_score & latest_rating iterable
    def __str__(self):
        for i in range(len(self.latest_rating)):
            print(f"{self.latest_scores[i]} {self.latest_rating[i]}")

    def plot_data(self):
        plot_data(self.latest_rating, self.latest_scores, self.name)

    def calculate_rating(self):
        return convert_ratings_to_dict(self.latest_rating, self.latest_scores)

    def store_data(self):
        pass  # pickle

    def load_data(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
