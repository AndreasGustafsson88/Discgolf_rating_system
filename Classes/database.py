from data_functions.get_ext_data import course_stats
from data_functions.handle_data import convert_ratings_to_dict, calc_average_by_hole, sort_by_diff
from data_functions.save_and_load import store_hole_stats, load_hole_stats, player_data, course_data


class Database:
    def __init__(self, name):
        self.name = name
        self.hole_stats = []
        self.courses = []
        self.players = []

    @staticmethod
    def get_throws(player, course):
        player = player_data(player)
        rating, score = course_data(course)
        score_dict = convert_ratings_to_dict(rating, score, calc_player=True)
        for k, v in score_dict.items():
            if player.rating == v:
                print(int(round(k)))

    @staticmethod
    def load_player(full_name):
        return player_data(full_name)

    def get_hole_average(self, sort=True):
        stats = calc_average_by_hole(self.hole_stats)
        if sort:
            stats = sort_by_diff(stats)
        for i in stats:
            print(i)

    def all_overview(self, file_name, show=True):
        self.hole_stats = course_stats(file_name)
        print("\n".join(f"{key}: {self.hole_stats[key]}" for key in self.hole_stats.keys() if show))
        return self.hole_stats

    def store_hole_overview(self, name):
        store_hole_stats(self.hole_stats, name)
        print("Save successful")

    def load_hole_overview(self):
        self.hole_stats = load_hole_stats()
        print("Load successful")



    def save_database(self):
        pass

    def load_database(self):
        pass

    def calc_hole_average(self):
        pass

    def update_database(self):
        # create new database and compare to main
        pass

    def show_courses(self):
        pass

    def show_players(self):
        pass

    def plot_course(self):
        pass

    def plot_player(self):
        pass
