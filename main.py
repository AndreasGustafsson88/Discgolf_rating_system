"""
Program that calculates a discgolf rating and convert that to a points system based on hole difficulty.
rating is based on previous PDGA competitions on chosen course and layout.
"""

from Classes.courses import Course
from Classes.database import Database
from Classes.players import Player
from data_functions.save_and_load import player_data, course_data


def skynet_v_0001():
    # stovner = Course("Stovner Discgolfpark Main", "Oslo")
    # stovner.get_data("https://www.pdga.com/tour/event/41183")
    # stovner.load_data()
    # stovner.merge_all()
    # holmenkollen.load_data()
    # holmenkollen.merge_all()
    skatås = Course("Skatås Main", "Gothenburg")
    slottskogen = Course("Slottskogen 22 Hole Course", "Gothenburg")

    krokhol = Course("Krokhol Disc Golf Course Krokhol Regular Layout", "Oslo")
    # ymer.get_data("https://www.pdga.com/tour/event/41059")
    # krokhol.get_data("https://www.pdga.com/tour/event/42664")
    krokhol.load_data()
    ale = Course("Ale Disc Golf Center White Course White", "gbg")
    # krokhol.plot_data()
    # krokhol.show_course_rating()
    # skatås = Course("skatås", "Gbg")
    # skatås.get_data("https://www.pdga.com/tour/event/41900")
    # skatås.plot_data()

    # ymer.plot_data()
    # ymer.plot_data()
    # gässlösa = Course("Gässlösa DGB Hole 1-18 (2020)", "Borås")
    # gässlösa.load_data()
    # gässlösa.plot_data()
    # gässlösa.merge_all()

    andreas = Player("Andreas", "Gustafsson")
    andreas.enter_data("Stovner Discgolfpark Main", [45, 55, 65])
    print(andreas.player_scores)
    andreas.load_player()
    benjamin = Player("Benjamin", "something")
    benjamin.load_player()
    print(benjamin.player_scores)
    benjamin.calc_rating(course="Stovner Discgolfpark Main")
    # andreas.load_player()
    # andreas.calc_rating()

    main_db = Database("main")

    main_db.update_database()

    main_db.show_courses()
    main_db.show_players(ranked=True)



    # main_db.player_history("Marius Dydland")
    # main_db.get_throws("Daniel Johansson", "Krokhol Disc Golf Course Krokhol Regular Layout")

    # main_db.all_overview("karl persson")

    # main_db.store_hole_overview("karl persson")
    # main_db.store_hole_overview("andreas")

    main_db.get_throws("Marius Dydland", "Stovner Discgolfpark Main")
    main_db.get_throws("Marius Dydland", "Holmenkollen DiscGolfpark Normal Oppsett")
    main_db.get_throws("Marius Dydland", "Gässlösa DGB Hole 1-18 (2020)")
    andreas.overview("andreas")
    main_db.get_throws("Andreas Gustafsson", "Ale Disc Golf Center White Course White")
    main_db.get_hole_average(course="Krokhol Disc Golf Course Krokhol Regular Layout")
    # for k in main_db.hole_stats.keys():
    #    print(f"{k}: {main_db.hole_stats[k]}")
    # print(main_db.hole_stats)
    # main_db.get_hole_average()
    # print(main_db.hole_difficulty)
    # main_db.store_ hole_overview("andreas")
    # andreas.all_overview("andreas")


if __name__ == "__main__":
    skynet_v_0001()
