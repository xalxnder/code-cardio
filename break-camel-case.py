'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example:
solution("camelCasing")  ==  "camel Casing"
'''
def solution(s):
    final = ""
    for letter in s:
        if letter.isupper():
            final += " "
        final += letter
    return final
			


print(solution("hello WorldCase"))