from data_functions.get_ext_data import read_csv
import statistics

from data_functions.handle_data import convert_ratings_to_dict
from data_functions.save_and_load import store_player_data, player_data, get_rating


class Player:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.player_scores = {}
        self.rating = []

    def calc_rating(self):
        self.rating = get_rating(self.player_scores)
        return int(statistics.mean(self.rating))

    def load_data(self):
        self.player_scores = player_data(f"{self.first_name} {self.last_name}")
        return self.player_scores

    def save_data(self):
        store_player_data(f"{self.first_name} {self.last_name}", self.player_scores)

    def get_data(self, file_name):
        self.player_scores = read_csv(file_name)
        return self.player_scores

    def enter_data(self, name, result):
        self.player_scores = {name: result}
        return self.player_scores

    def calc_average(self):
        average = self.player_scores.copy()
        for items in self.player_scores:
            average[items] = int(statistics.mean(average[items]))
        return average

    # Onödig function?
    # def calc_average(self): # FÖRKORTA OVANSTOENDE FUNCTION!
    #     average = self.player_scores.copy()

