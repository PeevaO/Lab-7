import numpy as np
import random as rd
from time import perf_counter

AMOUNT_NUMBERS = 10 ** 6


def create_data():
    list1 = [rd.random() for _ in range(AMOUNT_NUMBERS)]
    list2 = [rd.random() for _ in range(AMOUNT_NUMBERS)]
    return list1, list2


def elementwise_multiply(list1, list2):
    start_time = perf_counter()
    multiply = [list1[i] * list2[i] for i in range(AMOUNT_NUMBERS)]
    end_time = perf_counter()
    result_time = end_time - start_time
    return result_time


def numpy_multiply(list1, list2):
    array1 = np.array(list1)
    array2 = np.array(list2)
    start_time = perf_counter()
    multiply = np.multiply(array1, array2)
    end_time = perf_counter()
    result_time = end_time - start_time
    return result_time


def show_result():
    list1, list2 = create_data()
    result_elementwise = elementwise_multiply(list1, list2)
    result_numpy = numpy_multiply(list1, list2)

    if result_numpy < result_elementwise:
        print(f'Перемножение массивов с помощью NumPy быстрее на {result_elementwise - result_numpy} c.')
    else:
        print(f'Перемножение массивов с помощью NumPy медленнее на {result_numpy - result_elementwise} c.')


if __name__ == "__main__":
    show_result()
