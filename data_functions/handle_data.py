from itertools import chain
import numpy as np


def clean_raw_data(raw_data): # FIX THIS SHIT, lol!!
    temp1 = [i.split("\n") for i in raw_data[1:]]
    temp2 = [i.split() for j in [item[1:] for item in temp1] for i in j]
    result = []
    res = []
    if len(temp2[0]) >= 14:
        for i in temp2:
            if i[1].isalpha():
                try:
                    result.append([i[6], i[4], i[8], i[4], i[4], i[10]])
                except IndexError:
                    continue
            elif not i[1].isalpha():
                try:
                    result.append([i[7], i[5], i[9], i[5], i[11], i[5]])
                except IndexError:
                    continue
    else:
        for i in temp2:
            if i[1].isalpha():
                try:
                    result.append([i[6], i[4], i[8], i[4]])
                except IndexError:
                    continue
            elif not i[1].isalpha():
                try:
                    result.append([i[7], i[5], i[9], i[5]])
                except IndexError:
                    continue

    for i in result:
        if 30 < int(i[0]) < 100 and 650 < int(i[1]) < 1200:
            res.append(i)
    return res


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






