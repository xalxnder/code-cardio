"""
Given an array of integers , Find the minimum sum which is obtained from summing each Two integers product .ß
"""
def min_sum(arr):
    sorted_arr = sorted(arr)
    return sum([num * sorted_arr.pop() for num in sorted_arr])

print(min_sum([5,4,2,3]))