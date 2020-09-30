from itertools import chain
import numpy as np


def clean_raw_data(raw_data, pdga_numbers=False): # FIX THIS SHIT, lol!!
    temp_data = [item.split() for i in range(1, len(raw_data)) for item in raw_data[i].split("\n")]

    if not pdga_numbers:
        return [[i[6], i[4], i[8], i[4]] if len(i) > 9 else ["Invalid"] for i in temp_data]
    else:
        return [[i[6], i[7], i[8], i[9]] if len(i) > 9 else ["Invalid"] for i in temp_data]


def convert_to_int(s):
    return [list(map(int, item)) for item in s if item[0].isnumeric()]


def split_list(s):  # Split into two list that can represent x, y graph in Matplotlib.pyplot
    return list(chain.from_iterable([i[0::2] for i in s if 30 < i[0] < 200])), \
           list(chain.from_iterable([i[1::2] for i in s if 30 < i[0] < 200]))


def convert_ratings_to_dict(rating, score): # make 1 func to calculate average? it´s being used in two places
    coef = np.polyfit(rating, score, 1)
    predicted_ratings = [i for i in range(650, 1040)]
    predicted = list(map(int, np.polyval(coef, predicted_ratings)))

    return {predicted[i]: predicted_ratings[i] for i in range(len(predicted))}






