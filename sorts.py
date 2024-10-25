import random


def selection_sort(array, arr_size):
    for i in range(arr_size):
        min_index = i

        for j in range(i + 1, arr_size):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])


def insertion_sort(array, arr_size):
    for i in range(1, arr_size):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def bubble_sort(array, arr_size):
    for n in range(arr_size - 1, 0, -1):
        swapped = False
        for i in range(n):
            if array[i] > array[i + 1]:
                swapped = True
                array[i], array[i + 1] = array[i + 1], array[i]
        if not swapped:
            break


def merge(M, L, array):
    i = j = k = 0
    while i < len(L) and j < len(M):
        if L[i] < M[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = M[j]
            j += 1
        k += 1

    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1

    while j < len(M):
        array[k] = M[j]
        j += 1
        k += 1


def merge_sort(array, arr_size):
    if arr_size > 1:

        r = arr_size//2
        L = array[:r]
        M = array[r:]

        merge_sort(L, len(L))
        merge_sort(M, len(L))

        merge(M, L, array)


def shell_sort(array, arr_size):
    step = arr_size // 2
    while step > 0:
        for i in range(step, arr_size, 1):
            j = i
            delta = j - step
            while delta >= 0 and array[delta] > array[j]:
                array[delta], array[j] = array[j], array[delta]
                j = delta
                delta = j - step
        step //= 2


def hibbard_increment(n):
    increments = []
    k = 1
    while True:
        increment = (2 ** k) - 1
        if increment >= n:
            break
        increments.append(increment)
        k += 1
    return increments


def shell_sort_hibbard(array, arr_size):
    steps = hibbard_increment(arr_size)

    for step in reversed(steps):
        for i in range(step, arr_size):
            j = i
            delta = j - step
            while delta >= 0 and array[delta] > array[j]:
                array[delta], array[j] = array[j], array[delta]
                j = delta
                delta = j - step


def pratt_increment(n):
    increments = []
    i = 0
    while True:
        j = 0
        while True:
            increment = (2 ** i) * (3 ** j)
            if increment >= n:
                break
            increments.append(increment)
            j += 1
            if j > 10:
                break
        if increments and increments[-1] >= n:
            break
        i += 1
        if i > 16:
            break

    increments = list(sorted(set(increments)))
    return increments

def shell_sort_pratt(arr, arr_size):
    steps = pratt_increment(arr_size)

    for step in reversed(steps):
        for i in range(step, arr_size):
            j = i
            delta = j - step
            while delta >= 0 and arr[delta] > arr[j]:
                arr[delta], arr[j] = arr[j], arr[delta]
                j = delta
                delta = j - step


def quick_sort(array, arr_size):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = []
    middle = []
    right = []

    for x in array:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left, arr_size) + middle + quick_sort(right, arr_size)


def max_heapify(A, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and A[left] > A[largest]:
        largest = left
    if right < heap_size and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, heap_size, largest)

def build_heap(A):
    heap_size = len(A)
    for i in range((heap_size // 2), -1, -1):
        max_heapify(A, heap_size, i)

def heap_sort(array, arr_size):
    build_heap(array)
    for i in range(arr_size - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        arr_size -= 1
        max_heapify(array, arr_size, 0)