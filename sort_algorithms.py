import timeit
import numpy as np



# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
    return arr

# Генерація наборів даних
random_data = np.random.randint(1, 10000, 1000)
almost_sorted_data = sorted(random_data)
almost_sorted_data[499:501] = almost_sorted_data[501], almost_sorted_data[499]

# Вимірювання часу виконання
time_insertion = timeit.timeit('insertion_sort(random_data.copy())', globals=globals(), number=10)
time_merge = timeit.timeit('merge_sort(random_data.copy())', globals=globals(), number=10)
time_timsort = timeit.timeit('sorted(random_data)', globals=globals(), number=10)

time_insertion_almost_sorted = timeit.timeit('insertion_sort(almost_sorted_data.copy())', globals=globals(), number=10)
time_merge_almost_sorted = timeit.timeit('merge_sort(almost_sorted_data.copy())', globals=globals(), number=10)
time_timsort_almost_sorted = timeit.timeit('sorted(almost_sorted_data)', globals=globals(), number=10)



def main():
    print(f'time insertion: {time_insertion:.5F}')
    print(f'time merge: {time_merge:.5F}')
    print(f'time timsort: {time_timsort:.5F}\n')
    print(f'time insertion almost sorted: {time_insertion_almost_sorted:.5F}')
    print(f'time merge almost sorted: {time_merge_almost_sorted:.5F}')
    print(f'time timsort almost sorted: {time_timsort_almost_sorted:.5F}')



if __name__ == "__main__":
    main()