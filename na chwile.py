def sum_of_differences(arr):
    return max(arr) - min(arr) if arr else 0
    # if len(arr) < 2:
    #     return 0
    # s = sorted(arr)[::-1]
    # sum = 0
    # for i in range(1, len(s)):
    #     sum += s[i-1] - s[i]
    #
    # return sum


print(sum_of_differences([-3,-2,-1, -1]))