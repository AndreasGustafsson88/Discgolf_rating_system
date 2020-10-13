import os

from data_functions.get_ext_data import read_csv, sort_rounds, course_stats
import statistics

from data_functions.handle_data import convert_ratings_to_dict
from data_functions.save_and_load import store_player_data, player_data, get_rating

COURSE_DATA_PATH = "C:\\Kod\\Projekt\\Handicap system for Discgolf\\Course_data"


class Player:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.player_scores = [] # Change to list?
        self.rating = []

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def overview(file_name):
        all_data = read_csv(file_name)
        for key in all_data:
            print(f"{key}: {all_data[key]}")

    def calc_rating(self, rounds=20, course=""): # Would like to get acutal rounds if not 20
        rating, rounds = get_rating(self.player_scores, rounds, course)
        self.rating = int(statistics.mean(rating))
        print(f"{self.full_name} is rated {self.rating} from the previous {rounds} rounds")

    def load_player(self):
        all_data = player_data(f"{self.first_name} {self.last_name}")
        self.player_scores = all_data.player_scores

    def save_data(self):
        store_player_data(f"{self.first_name} {self.last_name}", self.player_scores)

    def save_player(self, player):
        store_player_data(f"{self.first_name} {self.last_name}", player)

    def get_data(self, file_name):
        self.player_scores = sort_rounds(file_name)
        return self.player_scores

    # TESTCASE METODEN, BLEV ANINGEN RÖRIG EFTER ATT JAG FÖRSÖKT ANPASSA DEN
    def enter_data(self, name, result, date=""):
        if len(result) < 1:
            raise ValueError("Enter valid score")
        match = [name for path, fol_list, files in os.walk(COURSE_DATA_PATH) for folder in fol_list if name == folder]
        if len(match) == 1:
            for res in result:
                if isinstance(res, int):
                    rating, _ = get_rating([[match[0], date, res]], rounds=20, course="")
                    if isinstance(rating, list):
                        self.player_scores.append([match[0], date, res])
                        self.rating += rating
                else:
                    raise ValueError(f"input {res} is not a valid input. Must be int format")
            if len(self.rating) < len(result):
                raise ValueError("The round mentioned above is either rated too high or low")
            return self.player_scores
        raise KeyError("Course and/or layout doesn't exist in the current database")

    def calc_average(self):
        average = self.player_scores.copy()
        for items in self.player_scores:
            average[items] = int(statistics.mean(average[items]))
        return average

    # Onödig function?
    # def calc_average(self): # FÖRKORTA OVANSTOENDE FUNCTION!
    #     average = self.player_scores.copy()

