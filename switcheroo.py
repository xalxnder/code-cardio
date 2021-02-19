'''
Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
'''


def switcheroo(string):
    new = list(string)
    for count, letter in enumerate(new):
        if letter == 'a':
            new[count] = 'b'
        elif letter == 'b':
            new[count] = 'a'
    return(''.join(new))

print(switcheroo("ccccc"))