"""
Program that calculates a discgolfcource rating based on previus PDGA competitions on chosen course and layout
"""

from Classes.courses import Course
from Classes.database import Database
from Classes.players import Player
from data_functions.save_and_load import player_data, course_data


def main():

    # krokhol = Course("Krokhol Disc Golf Course Krokhol Regular Layout", "Oslo")
    # ymer.get_data("https://www.pdga.com/tour/event/41059")
    # krokhol.get_data("https://www.pdga.com/tour/event/42664")
    # krokhol.load_data()
    # krokhol.plot_data()

    # ymer.plot_data()
    # ymer.plot_data()
    # gässlösa = Course("Gässlösa DGB Hole 1-18 (2020)", "Borås")
    # gässlösa.load_data()
    # gässlösa.plot_data()
    # gässlösa.merge_all()

    andreas = Player("Andreas", "Gustafsson")
    andreas.get_data("andreas")
    print(andreas.player_scores)
    andreas.calc_rating()

    joakim = Player("Joakim", "Wassberg")
    joakim.enter_data("Ymergårdens Discgolfcenter 2020 tournament layout", "202020", [58, 55])
    joakim.calc_rating()

    main_db = Database("main")
    main_db.update_database()
    # main_db.all_overview("karl persson")
    # main_db.all_overview("andreas")
    # main_db.store_hole_overview("karl persson")
    # main_db.store_hole_overview("andreas")

    main_db.get_throws("Andreas Gustafsson", "Ymergårdens Discgolfcenter 2020 tournament layout")
    main_db.get_throws("Karl Persson", "Gässlösa DGB Hole 1-18 (2020)")
    main_db.get_throws("Karl Persson", "Ymergårdens Discgolfcenter 2020 tournament layout")
    # for k in main_db.hole_stats.keys():
    #    print(f"{k}: {main_db.hole_stats[k]}")
    # print(main_db.hole_stats)
    # main_db.get_hole_average()
    # print(main_db.hole_difficulty)
    # main_db.store_ hole_overview("andreas")
    # andreas.all_overview("andreas")


if __name__ == "__main__":
    main()
