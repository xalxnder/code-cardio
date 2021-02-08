vowels = ['e','i','o','u']
def gordon(a):
    arr = a.split()
    final = []
    for word in arr:
        for letter in word:
            if letter == 'a' or letter == 'A':
                word = word.replace(letter, '@')
            if letter.lower() in vowels:
                word = word.replace(letter,'*')
        final.append(word.upper() + '!!!!')
    return ' '.join(final)

print(gordon('What feck damn cake'))