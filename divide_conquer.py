'''
Given a mixed array of number and string representations of integers, add up the string integers and subtract this from the total of the non-string integers.

Return as a number.
'''

def div_con(x):
    sum_strings = sum([int(num) for num in x if type(num)==str])
    non_strings = sum([int(num) for num in x if type(num)==int])
    return non_strings - sum_strings

div_con([9, 3, '7', '3'])