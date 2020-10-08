from data_functions.get_ext_data import course_stats
from data_functions.graph_rating_score import plot_player
from data_functions.handle_data import convert_ratings_to_dict, calc_average_by_hole, sort_by_diff
from data_functions.save_and_load import store_hole_stats, load_hole_stats, player_data, course_data, get_rating


class Database:
    def __init__(self, name):
        self.name = name
        self.hole_stats = []
        self.courses = []
        self.players = []
        self.hole_difficulty = []

    @staticmethod
    def load_player(full_name):
        return player_data(full_name)

    def get_throws(self, player, course):
        player = player_data(player)
        rating, score = course_data(course)
        score_dict = convert_ratings_to_dict(rating, score, calc_player=True)
        throws = [int(round(k)) for k, v in score_dict.items() if player.rating == v]
        for i in self.hole_difficulty:
            if course in i[0]:
                difference = throws[0] - i[1][0]
                if difference > 0:
                    holes = [i[j][0] for j in range(2, difference + 2)]
                    print(f"{player.first_name} {player.last_name} currently rated {player.rating}. {course}, par {i[1][0]}, is a though one, you get 1 extra throw "
                          f"on hole {holes}")
                if difference < 0:
                    holes = [i[j][0] for j in range(-1, difference - 1, -1)]
                    print(f"{player.first_name} {player.last_name} currently rated {player.rating}. {course}, par {i[1][0]}, is cake for someone of your caliber! "
                          f"you need a birdie on {holes}")
                if difference == 0:
                    print(f"{player.first_name} {player.last_name} currently rated {player.rating}. {course}, par {i[1][0]}, is just like its made for you! "
                          f"Just get through this on par and you´ll be fine")

    def player_history(self, name, course=""):
        player = self.load_player(name)
        rating_date = get_rating(player.player_scores, 20, course, plot=True)
        plot_player(name, rating_date)

    def get_hole_average(self, sort=True):
        if sort:
            self.hole_difficulty = sort_by_diff(self.hole_difficulty)
        print("\n".join(f"{i}" for i in self.hole_difficulty))

    def all_overview(self, file_name, show=True):
        self.hole_stats = course_stats(file_name)
        print("\n".join(f"{key}: {self.hole_stats[key]}" for key in self.hole_stats.keys() if show))
        return self.hole_stats

    def store_hole_overview(self, name):
        store_hole_stats(self.hole_stats, name)
        print("Save successful")

    def update_database(self):
        self.hole_stats = load_hole_stats()
        self.hole_difficulty = calc_average_by_hole(self.hole_stats)
        print("database updated successfully")

    def save_database(self):
        pass

    def calc_hole_average(self):
        pass

    def show_courses(self):
        pass

    def show_players(self):
        pass

    def plot_course(self):
        pass

    def plot_player(self):
        pass
