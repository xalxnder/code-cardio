'''
Description:
Gordon Ramsay shouts. He shouts and swears. There may be something wrong with him.
Anyway, you will be given a string of four words. Your job is to turn them in to Gordon language.

Rules:
Obviously the words should be Caps, Every word should end with '!!!!', Any letter 'a' or 'A' should become '@', Any other vowel should become '*'.
'''
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