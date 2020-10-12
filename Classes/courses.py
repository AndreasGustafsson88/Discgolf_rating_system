from data_functions import handle_data
from data_functions.get_ext_data import download
from data_functions.graph_rating_score import plot_data
from data_functions.handle_data import convert_ratings_to_dict, clean_raw_data
from data_functions.save_and_load import store_course_data, course_data

DRIVER_PATH = "C:\\Program Files (x86)\\Webdrivers\\chromedriver.exe"


class Course:
    def __init__(self, name, location, num_holes=18):
        self.name = name
        self.location = location
        self.num_holes = num_holes
        self.data = []
        self.latest_scores, self.latest_rating = [], []
        self.course_rating = []

    def __str__(self):
        for i in range(len(self.latest_rating)):
            print(f"{self.latest_scores[i]} {self.latest_rating[i]}")

    def get_data(self, link):
        print("Getting raw data")
        score, rating = download(link)
        self.latest_scores, self.latest_rating = clean_raw_data(score, rating)
        print("Data download complete!")

    def plot_data(self):
        plot_data(self.latest_rating, self.latest_scores, self.name)

    def show_course_rating(self):
        print("\n".join(f"{key}: {self.course_rating[key]}" for key in self.course_rating))

    def save_data(self, event_link):
        store_course_data(self.name, self.latest_rating, self.latest_scores, event_link)
        print("Save successful")

    def load_data(self):
        self.latest_rating, self.latest_scores = course_data(self.name)
        self.course_rating = convert_ratings_to_dict(self.latest_rating, self.latest_scores)
        print("Course data loaded successfully")

    def merge_all(self):
        store_course_data(self.name, self.latest_rating, self.latest_scores)

