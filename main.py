"""
Program that calculates a discgolfcource rating based on previus PDGA competitions on chosen course and layout
"""

from Classes.courses import Course
from Classes.database import Database
from Classes.players import Player
from data_functions.save_and_load import player_data, course_data


def main():
    # stovner = Course("Stovner Discgolfpark Main", "Oslo")
    # stovner.get_data("https://www.pdga.com/tour/event/41183")
    # stovner.load_data()
    # stovner.merge_all()
    # holmenkollen.load_data()
    # holmenkollen.merge_all()

    krokhol = Course("Krokhol Disc Golf Course Krokhol Regular Layout", "Oslo")
    # ymer.get_data("https://www.pdga.com/tour/event/41059")
    # krokhol.get_data("https://www.pdga.com/tour/event/42664")
    krokhol.load_data()
    # krokhol.plot_data()
    # krokhol.show_course_rating()

    # ymer.plot_data()
    # ymer.plot_data()
    # gässlösa = Course("Gässlösa DGB Hole 1-18 (2020)", "Borås")
    # gässlösa.load_data()
    # gässlösa.plot_data()
    # gässlösa.merge_all()

    # andreas.load_player()
    # andreas.calc_rating()

    main_db = Database("main")

    main_db.update_database()

    main_db.show_courses()
    main_db.show_players(ranked=True)

    main_db.get_throws("Benjamin something", "Stovner Discgolfpark Main")
    main_db.get_throws("Daniel Johansson", "Stovner Discgolfpark Main")
    main_db.get_throws("Daniel Johansson", "Krokhol Disc Golf Course Krokhol Regular Layout")
    # main_db.player_history("Marius Dydland")
    # main_db.get_throws("Daniel Johansson", "Krokhol Disc Golf Course Krokhol Regular Layout")

    # main_db.all_overview("karl persson")
    # main_db.all_overview("andreas")
    # main_db.store_hole_overview("karl persson")
    # main_db.store_hole_overview("andreas")

    main_db.get_throws("Marius Dydland", "Krokhol Disc Golf Course Krokhol Regular Layout")
    # main_db.get_throws("Marius Dydland", "Stovner Discgolfpark Main")
    # main_db.get_throws("Marius Dydland", "Holmenkollen DiscGolfpark Normal Oppsett")
    # main_db.get_throws("Marius Dydland", "Gässlösa DGB Hole 1-18 (2020)")
    # for k in main_db.hole_stats.keys():
    #    print(f"{k}: {main_db.hole_stats[k]}")
    # print(main_db.hole_stats)
    # main_db.get_hole_average()
    # print(main_db.hole_difficulty)
    # main_db.store_ hole_overview("andreas")
    # andreas.all_overview("andreas")


if __name__ == "__main__":
    main()
