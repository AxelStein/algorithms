word = list("rodeo")
size = len(word)


def rotate(s):
    pos = size - s
    tmp = word[pos]
    for i in range(pos + 1, size):
        word[i - 1] = word[i]
    word[size - 1] = tmp


def anagram(s):
    if s == 1:
        return
    for i in range(s):
        anagram(i)
        print(word)
        rotate(s)


anagram(size)
