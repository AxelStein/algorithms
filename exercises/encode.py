from collections import defaultdict, Counter


def duplicate_encode(word):
    letters = defaultdict(int)
    word = word.lower()
    for l in word:
        letters[l] += 1
    out = []
    for l in word:
        out.append('(' if letters[l] == 1 else ')')
    return ''.join(out)


def duplicate_encode_2(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)


def duplicate_encode_3(word):
    word = word.lower()
    return ''.join([')' if word.count(char) > 1 else '(' for char in word])


print(duplicate_encode('recEde'))
print(duplicate_encode('(( @'))
print(duplicate_encode('recede'))
