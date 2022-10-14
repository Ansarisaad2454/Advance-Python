letter=['a','b','d','e','i','o']

def vowel(letter):
    vowels=['a','e','i','o','u']
    return True if letter in vowels else False

filter_vowels=filter(vowel,letter)

print(tuple(filter_vowels))
