def fibo(num):
    if num == 1 or num == 2:
        return 1
    return fibo(num-1) + fibo(num-2)


fibo_ans = fibo(4)
print(fibo_ans)


def sorted(array):
    size = len(array)
    if size <= 1:
        return True
    if array[0] > array[1]:
        return False
    small = sorted(array[1:])
    if small:
        return True
    else:
        return False


array = [1,2,3,4,5, 1]
print(sorted(array))


def sum_of_array(array):
    size = len(array)
    if size == 0:
        return 0
    if size == 1:
        return array[0]
    return array[0] + sum_of_array(array[1:])


array = [1, 2, 3, 4]
print(sum_of_array(array))


def check_number(array, x):
    size = len(array)
    if size == 0:
        return False
    if array[0] == x:
        return True
    return check_number(array[1:], x)


array = [1, 2, 3, 4]
print(check_number(array, 1))


def sorted_index(array, index=0):
    if len(array) <= 1:
        return True
    if index == len(array)-1 or index == len(array):
        return True
    if array[index] > array[index+1]:
        return False
    return sorted_index(array, index+1)


array = [1, 0]
print(sorted_index(array))


# First Index of a number
def first_index(array, number):
    length = len(array)
    # if index == length:
    #     return -1
    # if array[index] == number:
    #     return index
    # return first_index(array, number, index+1)
    if length == 0:
        return -1
    if array[0] == number:
        return 0
    small = first_index(array[1:], number)
    if small == -1:
        return -1
    else:
        return small+1


a = [9, 10, 10, 8, 8]
print(first_index(a, 8))


# Last Index of a number
def last_idex(arr, number):
    length = len(arr)
    if length == 0:
        return -1
    small = last_idex(arr[1:], number)
    if small == -1:
        if arr[0] == number:
            return 0
        else:
            return -1
    else:
        return small+1


def last_index(arr, number, index):
    if index < 0:
        return -1
    if arr[index] == number:
        return index
    return last_index(arr, number, index-1)


arr = [9, 8, 10, 4, 0]
print(last_idex(arr, 0))
print(last_index(arr, 0, len(arr)-1))