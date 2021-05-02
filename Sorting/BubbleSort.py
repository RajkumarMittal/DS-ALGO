def bubble_sort(array):
    length = len(array)
    if length <= 1:
        return array
    for i in range(length-1):
        for j in range(i+1, length):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def selection_sort(arr):
    if len(arr) <= 1:
        return arr
    


arr = [4, 3, 2, 1]
print(bubble_sort(arr))