def longest(array):
    if len(array) == 1:
        return 1
    count_max = []
    for i in range(len(array)-1):
        max_val = array[i]
        count = 1
        for j in range(i+1, len(array)):
            if array[j] > max_val:
                max_val = array[j]
                count += 1
                count_max.append(count)
            elif array[j] == max_val:
                count_max.append(1)
    return max(count_max)


n = int(input())
li = [int(ele) for ele in input().split()]
print(longest(li))
