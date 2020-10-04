from data_functions.get_ext_data import read_csv, sort_rounds, course_stats
import statistics

from data_functions.handle_data import convert_ratings_to_dict
from data_functions.save_and_load import store_player_data, player_data, get_rating


class Player:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.player_scores = {}
        self.rating = []

    @staticmethod
    def load_player(self, first_name, last_name):
        name = player_data(f"{first_name} {last_name}")
        return name

    @staticmethod # This belongs to its own class? Database, name main?
    def all_overview(file_name, store=False):
        all_data = course_stats(file_name)
        if not store:
            for key in all_data.keys():
                print(f"{key}: {all_data[key]}")
        else:
            return all_data

    @staticmethod
    def overview(file_name):
        all_data = read_csv(file_name)
        for key in all_data.keys():
            print(f"{key}: {all_data[key]}")

    def calc_rating(self, rounds=20, course=""):
        self.rating = int(statistics.mean(get_rating(self.player_scores, rounds, course)))
        print(self.rating)

    def load_player1(self):
        self.player_scores = player_data(f"{self.first_name} {self.last_name}")
        return self.player_scores

    def save_data(self):
        store_player_data(f"{self.first_name} {self.last_name}", self.player_scores)

    def save_player(self, player):
        store_player_data(f"{self.first_name} {self.last_name}", player)

    def get_data(self, file_name):
        self.player_scores = sort_rounds(file_name)
        return self.player_scores

    def enter_data(self, name, date, result):
        self.player_scores = [name, date, [result]]
        return self.player_scores

    def calc_average(self):
        average = self.player_scores.copy()
        for items in self.player_scores:
            average[items] = int(statistics.mean(average[items]))
        return average

    # Onödig function?
    # def calc_average(self): # FÖRKORTA OVANSTOENDE FUNCTION!
    #     average = self.player_scores.copy()

