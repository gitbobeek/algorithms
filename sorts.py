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


def merge_sort(array):
    if len(array) > 1:

        r = len(array)//2
        L = array[:r]
        M = array[r:]

        merge_sort(L)
        merge_sort(M)

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


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def quick_sort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quick_sort(s_nums) + e_nums + quick_sort(m_nums)