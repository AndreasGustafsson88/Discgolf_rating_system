"""
Program that calculates a discgolfcource rating based on previus PDGA competitions on chosen course and layout
"""

from Classes.courses import Course
from Classes.players import Player
from data_functions.save_and_load import player_data, course_data


def main():
    ymer = Course("Ymergårdens Discgolfcenter", "BORÅS")
    # ymer.get_data("https://www.pdga.com/tour/event/39351")
    # ymer.save_data("39351")
    # ymer.save_data("46819")

    # print(ymer.latest_scores)
    ymer.load_data()
    ymer.plot_data()
    print(ymer.calculate_rating())

    # andreas = Player("Andreas", "Gustafsson")
    # andreas.get_data("andreas")

    andreas = player_data("Andreas Gustafsson")
    # print(andreas.player_scores)
    # print(type(andreas))
    print(andreas.rating)
    andreas.save_player(andreas)
    # andreas.load_data()
    # for key in andreas.player_scores:
    #     print(f"{key}: {andreas.player_scores[key]}")



if __name__ == "__main__":
    main()
