'''
Oh no! The number has been mixed up with the text. Your goal is to retreive the number from the text, can you return the number back to it's original state?

Task
Your task is to return a number from a string
'''

def filter_string(string):
    return int(''.join([num for num in string if num.isdigit()]))
    



