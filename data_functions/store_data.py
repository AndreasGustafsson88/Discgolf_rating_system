import pickle
import os

COURSE_DATA_PATH = "C:\\Kod\\Projekt\\Handicap system for Discgolf\\Course_data"


def store_course_data(course_name, object1, object2, link):
    with open(f"{COURSE_DATA_PATH}\\{course_name}{link}.dat", "wb") as file:
        pickle.dump(object1, file)
        pickle.dump(object2, file)


def course_data(course_name, link):
    with open(f"{COURSE_DATA_PATH}\\{course_name}{link}.dat", "rb") as file:
        return pickle.load(file), pickle.load(file)
