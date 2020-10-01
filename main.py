"""
Program that calculates a discgolfcource rating based on previus PDGA competitions on chosen course and layout
"""

from Classes.courses import Course
from Classes.players import Player


def main():
    ymer = Course("Ymergårdens Discgolfcenter", "BORÅS")
    ymer.get_data("https://www.pdga.com/tour/event/42661")
    # ymer.save_data("39351")
    # ymer.load_data()
    # ymer.save_data("46819")
    ymer.plot_data()
    # print(ymer.latest_scores)
    # print(ymer.calculate_rating())

    # andreas = Player("Andreas", "Gustafsson")
    # andreas.get_data("andreas")
    # andreas.load_data()

    # print(andreas.calc_rating())



if __name__ == "__main__":
    main()
