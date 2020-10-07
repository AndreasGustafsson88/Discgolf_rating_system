"""
Program that calculates a discgolfcource rating based on previus PDGA competitions on chosen course and layout
"""

from Classes.courses import Course
from Classes.database import Database
from Classes.players import Player
from data_functions.save_and_load import player_data, course_data


def main():

    main_db = Database("main")
    main_db.load_hole_overview()
    main_db.get_hole_average(show=False)
    # main_db.all_overview("karl persson")
    # main_db.all_overview("andreas")
    # main_db.store_hole_overview("karl persson")
    # main_db.store_hole_overview("andreas")
    andreas = Player("Andreas", "Gustafsson")
    andreas.load_player()
    print(andreas.player_scores)
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
