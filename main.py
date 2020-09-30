"""
Program that calculates a discgolfcource rating based on previus PDGA competitions on chosen course and layout
"""

from Classes.courses import Course
from Classes.players import Player


def main():
    ymer = Course("YMERGÅRDEN", "BORÅS")
    # ymer.get_data("https://www.pdga.com/tour/event/46819")
    # ymer.plot_data()
    # ymer.store_data("46819")
    ymer.load_data("46819")
    ymer.plot_data()
    print(ymer.latest_rating)
    print(ymer.latest_scores)

    andreas = Player("Andreas", "Gustafsson")
    for item in andreas.player_scores:
        print(f"{item}: {andreas.player_scores[item]}")


if __name__ == "__main__":
    main()
