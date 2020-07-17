# iterating over an open file yields its lines, one by one

words = []
for line in open('../chapter3/words.txt', 'r'):
    words.append(line.strip().lower())

print(words.index('womble'))
