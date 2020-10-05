import pickle
import os
import collections.abc
from collections import defaultdict
from itertools import chain

from data_functions.handle_data import convert_ratings_to_dict

COURSE_DATA_PATH = "C:\\Kod\\Projekt\\Handicap system for Discgolf\\Course_data"
PLAYER_DATA_PATH = "C:\\Kod\\Projekt\\Handicap system for Discgolf\\Player_data"


def store_course_data(course_name, object1, object2, link="ALL_ROUNDS"):
    while True:
        try:
            with open(f"{COURSE_DATA_PATH}\\{course_name}\\{course_name} {link}.dat", "wb") as file:
                pickle.dump(object1, file)
                pickle.dump(object2, file)
                break
        except FileNotFoundError:
            os.makedirs(f"{COURSE_DATA_PATH}\\{course_name}")


def course_data(course_name):
    rating, score = [], []
    for path, sub_folder, file_list in os.walk(COURSE_DATA_PATH):
        for name in file_list:
            if course_name in name:
                with open(os.path.join(path, name), "rb") as file:
                    rating += pickle.load(file)
                    score += pickle.load(file)
    return rating, score


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


def get_rating(player_scores, rounds, course):
    ratings = []
    how_many_rounds = 0
    for values in player_scores:
        if how_many_rounds == rounds:
            return ratings
        for path, sub_folder, file_list in os.walk(COURSE_DATA_PATH):
            for name in file_list:
                if values[0] in name and "ALL_ROUNDS" in name and course in name:
                    with open(os.path.join(path, name), "rb") as file:
                        average = convert_ratings_to_dict(pickle.load(file), pickle.load(file))
                        ratings.append(average[values[2]])
                        how_many_rounds += 1
    return ratings


def store_hole_stats(data, name):
    with open(f"{COURSE_DATA_PATH}\\Hole_statistics\\{name}.dat", "wb") as file:
        pickle.dump(data, file)


def load_hole_stats():
    stats = defaultdict()
    for path, sub_folder, file_list in os.walk(f"{COURSE_DATA_PATH}\\Hole_statistics"):
        for file in file_list:
            with open(os.path.join(path, file), "rb") as stored:
                stored_stats = pickle.load(stored)
                for k, v in stored_stats.items():
                    if k not in stats.keys():
                        stats[k] = stored_stats[k]
                    else:
                        for key, val in v.items():
                            if not val == stats[k][key]:
                                for num in stored_stats[k][key][1]:
                                    stats[k][key][1].append(num)
    return stats


def update_dict(d, u):
    res_dict = defaultdict(dict)
    for k, v in u.items():
        if k not in d.keys():
            d.update(k)
        else:
            for key, val in v.items():
                if not val == d[key]:
                    d[k][key][1].append(u[k][key][1])
    return d
