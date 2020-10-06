"""
Program that calculates a discgolfcource rating based on previus PDGA competitions on chosen course and layout
"""

from Classes.courses import Course
from Classes.database import Database
from Classes.players import Player
from data_functions.save_and_load import player_data, course_data


def main():
    # gässlösa = Course("Gässlösa DGB", "BORÅS")
    # gässlösa.get_data("https://www.pdga.com/tour/event/40504")
    # gässlösa.save_data("40504")
    # gässlösa.load_data()
    # print(gässlösa.calculate_rating())
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
    # print(ymer.calculate_rating())
    # ymer.plot_data()
    # ymer.merge_all()
    # ymer.save_data("46819")

    # print(ymer.latest_scores)
    # ymer.load_data()
    # ymer.plot_data()
    # print(ymer.calculate_rating())




    main_db = Database("main")
    # main_db.all_overview("karl persson")
    # main_db.all_overview("andreas")
    # main_db.store_hole_overview("karl persson")
    # main_db.store_hole_overview("andreas")

    main_db.load_hole_overview()
    main_db.get_hole_average(show=False)
    main_db.get_throws("Andreas Gustafsson", "Krokhol Disc Golf Course")
    main_db.get_throws("Karl Persson", "Gässlösa DGB")
    main_db.get_throws("Karl Persson", "Ymergårdens Discgolfcenter")
    # for k in main_db.hole_stats.keys():
    #    print(f"{k}: {main_db.hole_stats[k]}")
    # print(main_db.hole_stats)
    # main_db.get_hole_average()
    # print(main_db.hole_difficulty)
    # main_db.store_ hole_overview("andreas")
    # andreas.all_overview("andreas")


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
