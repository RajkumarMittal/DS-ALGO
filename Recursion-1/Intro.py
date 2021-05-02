from sys import setrecursionlimit as sl
sl(11000)


def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)


def addition(num):
    if num == 0:
        return 0
    return num + addition(num-1)


def power(x, num):
    if num == 0:
        return 1
    return x * power(x, num-1)




n = int(input())
num1 = int(input())
factorial = fact(n)
add = addition(n)
po = power(num1, n)
print("The factorial is : " + str(factorial))
print("The sum is : " + str(add))
print(str(po))


