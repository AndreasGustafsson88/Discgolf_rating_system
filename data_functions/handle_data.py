from itertools import chain
import numpy as np


def filter_lists(clean_round, clean_rating):
    rating = [clean_rating[i] for i, val in enumerate(clean_rating) if val != 0]
    score = [clean_round[i] for i, val in enumerate(clean_rating) if val != 0]
    rating = [rating[i] for i, val in enumerate(score) if 10 < val < 120]
    score = [score[i] for i, val in enumerate(score) if 10 < val < 120]

    return score, rating


def clean_raw_data(score, rating):
    clean_round = [int(i) for i in score if i.isnumeric()]
    clean_rating = list(filter(lambda x: x.isnumeric(), (map(lambda x: "0" if x == "" else x, rating))))
    clean_rating = list(chain.from_iterable([[int(i), int(i)] for i in clean_rating]))

    return filter_lists(clean_round, clean_rating)


# def filter_list(result, res):
#     for i in result:
#         print(i)
#         try:
#             if 30 < int(i[0]) < 100 and 650 < int(i[1]) < 1200 and 30 < int(i[2]) < 100 and 30 < int(i[6]) < 100:
#                 res.append(i)
#         except IndexError:
#             try:
#                 if 30 < int(i[0]) < 100 and 650 < int(i[1]) < 1200 and 30 < int(i[2]) < 100:
#                     res.append(i)
#             except IndexError:
#                 if 30 < int(i[0]) < 100 and 650 < int(i[1]) < 1200:
#                     res.append(i)
#
#
# def clean_raw_data(raw_data): # FIX THIS SHIT, lol!!
#     temp1 = [i.split("\n") for i in raw_data[1:]]
#     temp2 = [i.split() for j in [item[1:] for item in temp1] for i in j]
#     result, res = [], []
#     heading = temp1[0][0]
#
#     if "Finals" in heading:
#         for i in temp2:
#             try:
#                 result.append([i[7], i[5], i[9], i[5], i[11], i[5], i[13], i[5]])
#             except IndexError:
#                 continue
#
#     if "Points" in heading and "Rd3" in heading:
#         for i in temp2:
#             try:
#                 result.append([i[7], i[5], i[9], i[5], i[11], i[5]])
#             except IndexError:
#                 continue
#
#     elif "Rd3" in heading:
#         for i in temp2:
#             try:
#                 result.append([i[6], i[4], i[8], i[4], i[4], i[10]])
#             except IndexError:
#                 continue
#
#     elif "Points" in heading and "Rd2" in heading:
#         for i in temp2:
#             try:
#                 result.append([i[7], i[5], i[9], i[5]])
#             except IndexError:
#                 continue
#
#     elif "Rd2" in heading:
#         for i in temp2:
#             try:
#                 result.append([i[6], i[4], i[8], i[4]])
#             except IndexError:
#                 continue
#
#     elif "Points" in heading:
#         for i in temp2:
#             try:
#                 result.append([i[7], i[5]])
#             except IndexError:
#                 continue
#
#     else:
#         for i in temp2:
#             try:
#                 result.append([i[6], i[4]])
#             except IndexError:
#                 continue
#
#     filter_list(result, res)
#     return res
#
#
# def convert_to_int(s):
#     return [list(map(int, item)) for item in s if item[0].isnumeric()]
#
#
# def split_list(s):  # Split into two list that can represent x, y graph in Matplotlib.pyplot
#     return list(chain.from_iterable([i[0::2] for i in s if 30 < i[0] < 200])), \
#            list(chain.from_iterable([i[1::2] for i in s if 30 < i[0] < 200]))


def convert_ratings_to_dict(rating, score, calc_player=False): # make 1 func to calculate average? it´s being used in two places
    coef = np.polyfit(rating, score, 1)
    predicted_ratings = [i for i in range(650, 1200)]
    if calc_player:
        predicted = list(np.polyval(coef, predicted_ratings))
    else:
        predicted = list(map(int, np.polyval(coef, predicted_ratings)))

    return {predicted[i]: predicted_ratings[i] for i in range(len(predicted))}


def calc_average_by_hole(s):
    d = []
    index = 0
    for k, v in s.items():
        d.append([k])
        sub_index = 2
        for key, value in s[k].items():
            if key == "PAR":
                d[index].append(s[k][key])
            elif value != [0, []]:
                d[index].append([f"{key}:", s[k][key][0], round(sum(s[k][key][1]) / len(s[k][key][1]), 2)])
                diff = round(d[index][sub_index][2] - d[index][sub_index][1], 2)
                d[index][sub_index].append(diff)
                sub_index += 1
        index += 1
    return d


def sort_by_diff(s):
    res = []
    for i in s:
        temp = i[2:]
        temp.sort(key=lambda x: x[3], reverse=True)
        res.append(i[:2] + temp)
    return res


def calc_average_by_hole1(s): # RETURNS A DICT BUT REALLY HARD TO SORT, CURRENTLY DOESN´T USE IT
    d = s
    for k, v in d.items():
        for key, value in d[k].items():
            if key == "PAR":
                continue
            elif value != [0, []]:
                d[k][key][1] = round(sum(d[k][key][1]) / len(d[k][key][1]), 2)
                res = round(d[k][key][1] - d[k][key][0], 2)
                d[k][key].append(res)
    print(d)
    return d




