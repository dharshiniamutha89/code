fileName = input()
inputFile = open(fileName,'r')
text = inputFile.read()
sentences = text.count('.')+text.count('?')+text.count(':')+text.count(';')+text.count('!')
words = len(text.split())
syllables = 0
for word in text.split():
    for vowel in ['a','e','i','o','u']:
         syllables += word.count(vowel)
    for ending in ['es','ed','e']:
    if word.endswith(ending):
      syllables -= 1
    if word.endswith('le'):
      syllables += 1
index = 5206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
level = 50.39 * (words / sentences)111.8 * (syllables / words) - 15.59
print(sentences)
print(words)
print(syllables)
print(index)
print(level)
