import random
import time
from sys import setrecursionlimit

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
setrecursionlimit(1000001)

import sorts
import array_creation_types as act


def make_function_graph(_sizes, _time_values, _act_name, _sort_name):
    # plt.figure()

    x = np.array(_sizes)
    y = np.array(_time_values)

    poly = PolynomialFeatures(degree=2, include_bias=False)
    poly_features = poly.fit_transform(x.reshape(-1, 1))
    poly_reg_model = LinearRegression()
    poly_reg_model.fit(poly_features, y)
    y_predicted = poly_reg_model.predict(poly_features)

    # plt.scatter(x, y, s=6, c="red", label="Values")
    plt.plot(x, y_predicted, label=_act_name, c=act_colors[_act_name])
    plt.legend()

    # plt.xlabel('Number of elements (N)')
    # plt.ylabel('Time (Seconds)')
    # plt.title(_sort_name)
    # plt.grid()


def show_graph(_sort_name):
    plt.xlabel('Number of elements (N)')
    plt.ylabel('Time (Seconds)')
    plt.title(_sort_name)
    plt.grid()
    plt.show()


act_colors = {
    "Random": "yellow",
    "Sorted": "purple",
    "Inverse Sorted": "red",
    "Nearly Sorted": "blue",
}


act_types = {
    "Random": act.create_random_array,
    "Sorted": act.create_sorted_array,
    "Inverse Sorted": act.create_inverse_sorted_array,
    "Nearly Sorted": act.create_90_10_array,
}


if __name__ == '__main__':
    random.seed(1)
    sizes = range(5000, 100000 + 1, 5000)

    sort_name = "Merge sort"

    for act_name, act_create in act_types.items():
        time_values = []
        print(f"{sort_name} for {act_name} array")
        for size in sizes:
            arr = act_create(size)
            sort_name = f"Merge sort for {act_name} array"

            start_time = time.perf_counter()
            sorts.merge_sort(arr, size)
            end_time = time.perf_counter()

            elapsed_time = end_time - start_time
            time_values.append(elapsed_time)


            print(f"{size} {elapsed_time:.3f}")

        # make_function_graph(sizes, time_values, act_name, sort_name)
    # show_graph(sort_name)