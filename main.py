"""
Program that calculates a discgolfcource rating based on previus PDGA competitions on chosen course and layout
"""

from Classes.courses import Course
from Classes.players import Player
from data_functions.save_and_load import player_data, course_data


def main():
    # gässlösa = Course("Gässlösa DGB", "BORÅS")
    # gässlösa.get_data("https://www.pdga.com/tour/event/40504")
    # gässlösa.save_data("40504")
    # gässlösa.load_data()
    # gässlösa.merge_all()
    # gässlösa.plot_data()
    # print(gässlösa.calculate_rating())
    # krokhol = Course("Krokhol Disc Golf Course", "OSLO")
    # krokhol.load_data()
    # krokhol.plot_data()
    # krokhol.merge_all()
    # ymer = Course("Ymergårdens Discgolfcenter", "BORÅS")
    # ymer.get_data("https://www.pdga.com/tour/event/39351")
    # ymer.load_data()
    # ymer.plot_data()
    # ymer.merge_all()
    # ymer.save_data("46819")

    # print(ymer.latest_scores)
    # ymer.load_data()
    # ymer.plot_data()
    # print(ymer.calculate_rating())

    andreas = Player("Andreas", "Gustafsson")
    andreas.get_data("andreas")


    andreas.all_overview("andreas")


    # andreas = player_data("Andreas Gustafsson")
    # print(andreas.player_scores)
    # print(type(andreas))
    # andreas.get_data("andreas")
    # andreas.save_data()
    # andreas.calc_rating()


    # print(andreas.rating)
    # andreas.save_player(andreas)
    # andreas.load_data()
    # for key in andreas.player_scores:
    #     print(f"{key}: {andreas.player_scores[key]}")


if __name__ == "__main__":
    main()
