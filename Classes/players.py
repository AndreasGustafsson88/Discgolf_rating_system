from datetime import datetime
from typing import List
from data_functions.get_ext_data import read_csv, sort_rounds, download
import statistics
from data_functions.save_and_load import store_player_data, player_data, get_rating, search_course


class Player:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.player_scores = []
        self._metrix_rating = 0
        self._pdga_rating = 0
        self.rating = 0

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def metrix_rating(self):
        return self._metrix_rating

    @metrix_rating.setter
    def metrix_rating(self, rating):
        self._metrix_rating = rating

    @staticmethod
    def overview(file_name):
        all_data = read_csv(file_name)
        for key in all_data:
            print(f"{key}: {all_data[key]}")

    @property
    def pdga_rating(self):
        return self._pdga_rating

    @pdga_rating.setter
    def pdga_rating(self, pdga_number):
        self._pdga_rating = download(pdga_number, pdga=True)

    def calc_rating(self, rounds=20, course=""):
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

    def enter_data(self, name: str, result: List[int], date=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")):
        """
        :param name: takes a string input, must be exact match of course in database. If not raises KeyError.

        :param result: Must be a list with int. If value is to low of high, raises ValueError. Will show which round
        is affected. !!! Round will still be added to player_score, don't save until fixed !!!

        :param date: default value is time right now with datetime module. IF you want to use database method
        player_history and enter date manually, format must be ""%Y-%m-%d %H:%M""

        :return: None. Scores and rating is added to player property.
        """
        # SEARCH FOR COURSE IN DATABASE, IF NO MATCH RAISES KEYERROR
        match = search_course(name)

        if len(match) == 1:
            all_rating = []
            for res in result:
                rating, _ = get_rating([[match[0], date, res]], rounds=20, course="")
                self.player_scores.append([name, date, res])
                all_rating += rating
            self.rating = int(statistics.mean(all_rating))

            # CHECK IF ALL ROUNDS WHERE ADDED, IF NOT THEN ROUND RESULT IS NOT VALID VALUE, EITHER TOO HIGH OR LOW
            if len(all_rating) < len(result):
                raise ValueError("The round mentioned above is either rated too high or low")

        else:
            raise KeyError("Course and/or layout doesn't exist in the current database")

    def calc_average(self):
        average = self.player_scores.copy()
        for items in self.player_scores:
            average[items] = int(statistics.mean(average[items]))
        return average
