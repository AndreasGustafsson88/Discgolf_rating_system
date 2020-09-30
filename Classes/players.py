from data_functions.get_data import read_csv
import statistics


class Player:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.player_scores = []
        self.rating = self.calc_rating()

    def calc_rating(self):
        pass

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

