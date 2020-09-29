import matplotlib.pyplot as plt
import numpy as np


def plot_data(rating, score, course, color="Blue", x_label="RATING", y_label="SCORE"):

    plt.scatter(rating, score, color=color)

    coef = np.polyfit(rating, score, 1)

    predicted_ratings = [i for i in range(650, 1040)]
    predicted = np.polyval(coef, predicted_ratings)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(course)
    plt.plot(predicted_ratings, predicted, lw=2, color="Black")

    plt.show()
