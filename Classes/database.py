from data_functions.get_ext_data import course_stats


class Database:
    def __init__(self, name):
        self.name = name
        self.hole_stats = []
        self.courses = []
        self.players = []

    @staticmethod
    def all_overview(file_name, store=False):
        all_data = course_stats(file_name)
        if not store:
            for key in all_data.keys():
                print(f"{key}: {all_data[key]}")
        else:
            return all_data

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

