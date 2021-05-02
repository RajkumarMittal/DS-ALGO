
# Determine if a string has all unique characters
def unique(string):
    string = string.lower()
    book = {}
    for char in string:
        if char not in book:
            book[char] = 1
        else:
            return False
    return True
    # for i in book:
    #     if book[i] >= 2:
    #         return False
    # return True


# user_input = input("Enter your string : ")
# print(unique(user_input))


# Check Permutation
def permutation(input_1, input_2):
    input_1 = input_1.lower()
    input_2 = input_2.lower()
    if len(input_1) != len(input_2):
        return False
    book1 = {}
    book2 = {}
    for char in input_1:
        if char not in book1:
            book1[char] = 1
        else:
            book1[char] += 1
    for char in input_2:
        if char not in book2:
            book2[char] = 1
        else:
            book2[char] += 1
    for i in book1:
        if book1[i] != book2[i]:
            return False
    return True


user_input_1 = input("Enter your 1st string : ")
user_input_2 = input("Enter your 2st string : ")
print(permutation(user_input_1, user_input_2))