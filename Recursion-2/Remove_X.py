# Remove X
def remove_x(string):
    length = len(string)
    if length == 0:
        return string
    small = remove_x(string[1:])
    if string[0] == "x":
        return small
    else:
        return string[0] + small


s = "axbcsx"
print(remove_x(s))


# Replace Pi
def replace_pi(string):
    if len(string) == 0 or len(string) == 1:
        return string
    small = replace_pi(string[1:])
    if string[:2] == "pi":
        return "3.14" + small[1:]
    else:
        return string[0] + small


s = "pippi"
print(replace_pi(s))


# Remove the consecutive duplicate
def remove_duplicate(s):
    if len(s) == 1 or len(s) == 0:
        return s
    small = remove_duplicate(s[1:])
    if s[0] == s[1]:
        return small
    else:
        return s[0] + small


s = "aabccba"
print(remove_duplicate(s))


# Binary Search
def binary(array, x):
    length = len(array)
    if length == 0:
        return False
    mid = length // 2
    if array[mid] == x:
        return True
    if array[mid] < x:
        return binary(array[mid+1:], x)
    else:
        return binary(array[:mid], x)


a = [1, 2, 3, 4, 5]
print(binary(a, 4))


# Merge sort
def merge(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    s1 = array[:mid]
    s2 = array[mid:]
    merge(s1)
    merge(s2)
    i = 0
    j = 0
    k = 0
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            array[k] = s1[i]
            i += 1
            k += 1
        else:
            array[k] = s2[j]
            j += 1
            k += 1
    while i < len(s1):
        array[k] = s1[i]
        i += 1
        k += 1

    while j < len(s2):
        array[k] = s2[j]
        j += 1
        k += 1


a = [2, 6, 8, 5, 4, 3]
merge(a)
print(a)


# Quick Sort
def partition(array, si, ei):
    pivot = array[si]
    count = 0
    # To find the correct place for pivot
    for i in range(si, ei+1):
        if array[i] < pivot:
            count += 1
    array[si + count], array[si] = array[si], array[si + count]
    pivot_index = si + count
    i = si
    j = ei
    while i < j:
        if array[i] < pivot:
            i += 1
        elif array[j] >= pivot:
            j -= 1
        else:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    return pivot_index


def quickSort(array, si, ei):
    # if len(array) == 1 or len(array) == 0:
    #     return array
    if si >= ei:
        return
    pivot_index = partition(array, si, ei)
    quickSort(array, si, pivot_index-1)
    quickSort(array, pivot_index+1, ei)


a = [2, 6, 8, 5, 4, 3]
quickSort(a, 0, len(a)-1)
print(a)




