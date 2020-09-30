import pickle
import os

from data_functions.handle_data import convert_ratings_to_dict

COURSE_DATA_PATH = "C:\\Kod\\Projekt\\Handicap system for Discgolf\\Course_data"
PLAYER_DATA_PATH = "C:\\Kod\\Projekt\\Handicap system for Discgolf\\Player_data"


def store_course_data(course_name, object1, object2, link):
    while True:
        try:
            with open(f"{COURSE_DATA_PATH}\\{course_name}\\{course_name}{link}.dat", "wb") as file:
                pickle.dump(object1, file)
                pickle.dump(object2, file)
                break
        except FileNotFoundError:
            os.makedirs(f"{COURSE_DATA_PATH}\\{course_name}")


def course_data(course_name):
    for path, sub_folder, file_list in os.walk(COURSE_DATA_PATH):
        for name in file_list:
            if course_name in name:
                with open(os.path.join(path, name), "rb") as file:
                    return pickle.load(file), pickle.load(file)


def store_player_data(player_name, object1):
    while True:
        try:
            with open(f"{PLAYER_DATA_PATH}\\{player_name}\\{player_name}.dat", "wb") as file:
                pickle.dump(object1, file)
                break

        except FileNotFoundError:
            os.makedirs(f"{PLAYER_DATA_PATH}\\{player_name}")


def player_data(player_name):
    for path, sub_folder, file_list in os.walk(PLAYER_DATA_PATH):
        for name in file_list:
            if player_name in name:
                with open(os.path.join(path, name), "rb") as file:
                    return pickle.load(file)


def get_rating(player_scores):
    ratings = []
    for key in player_scores.keys():
        for path, sub_folder, file_list in os.walk(COURSE_DATA_PATH):
            for name in file_list:
                if key in name:
                    with open(os.path.join(path, name), "rb") as file:
                        average = convert_ratings_to_dict(pickle.load(file), pickle.load(file))
                        for i, scores in enumerate(player_scores[key]):
                            if i < 7:
                                ratings.append(average[player_scores[key][i]])
    return ratings
