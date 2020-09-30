import pickle
import os

COURSE_DATA_PATH = "C:\\Kod\\Projekt\\Handicap system for Discgolf\\Course_data"


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
