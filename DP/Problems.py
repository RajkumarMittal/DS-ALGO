#
# def fibonacci_dp(num, dp):
#     if num == 1 or num == 2:
#         return num
#     if dp[num] == -1:
#         dp[num] = fibonacci_dp(num-1, dp) + fibonacci_dp(num-2, dp)
#     return dp[num]
#
#
# num = 5
# dp = [-1 for i in range(0, num+1)]
# print(fibonacci_dp(num, dp))


# Min step to 1
# def min_step(num, dp):
#     if num == 1:
#         return 0
#     if (num % 2 != 0 and num % 3 != 0) and dp[num] == -1:
#         dp[num] = min_step(num - 1, dp)
#
#
# num = int(input())
# dp = [-1 for i in range(num + 1)]
# print(min_step(num, dp))

