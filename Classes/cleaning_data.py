from itertools import chain


class CleaningData:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.clean_data = self.clean_raw_data()
        self.int_data = self.convert_to_int()
        self.scores, self.rating = self.split_list()

    def clean_raw_data(self, pdga_numbers=False):
        temp_data = [item.split() for item in self.raw_data[1].split("\n")]

        if not pdga_numbers:
            return [[i[6], i[4], i[8], i[4]] if len(i) > 9 else ["Invalid"] for i in temp_data]
        else:
            return [[i[6], i[7], i[8], i[9]] if len(i) > 9 else ["Invalid"] for i in temp_data]

    def convert_to_int(self):
        return [list(map(int, item)) for item in self.clean_data if item[0].isnumeric()]

    def split_list(self):  # Split into two list that can represent x, y graph in Matplotlib.pyplot
        return list(chain.from_iterable([i[0::2] for i in self.int_data if 30 < i[0] < 200])), \
               list(chain.from_iterable([i[1::2] for i in self.int_data if 30 < i[0] < 200]))
