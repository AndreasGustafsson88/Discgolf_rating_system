"""
Program that calculates a discgolfcource rating based on previus PDGA competitions on chosen course and layout
"""

from Classes.courses import Course
from Classes.players import Player


def main():
    ymer = Course("Ymergårdens Discgolfcenter", "BORÅS")
    # ymer.get_data("https://www.pdga.com/tour/event/46819")
    # ymer.store_data("46819")
    ymer.load_data()
    # ymer.store_data("46819")
    ymer.plot_data()
    # print(ymer.latest_scores)
    # print(ymer.calculate_rating())

    # andreas = Player("Andreas", "Gustafsson")
    # andreas.get_data("andreas")
    # for key in andreas.player_scores:
    #     print(f"{key}: {andreas.player_scores[key]}")



if __name__ == "__main__":
    main()
