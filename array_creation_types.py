import random


def create_random_array(N):
    # return [random.randint(0, 500) for _ in range(N)]
    _arr = [_ for _ in range(N)]
    random.shuffle(_arr)
    return _arr


def create_sorted_array(N):
    return [_ for _ in range(N)]


def create_inverse_sorted_array(N):
    return [_ for _ in range(N, 0, -1)]


def create_90_10_array(N):
    return [_ for _ in range(N // 10 * 9)] + [random.randint(0, 500) for _ in range((N // 10), 0, -1)]
