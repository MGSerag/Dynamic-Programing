def word_to_num(word):
    num = {ch: idx + 1 for idx, ch in enumerate("abcdefghijklmnopqrstuvwxyz")}
    return sum([num[ch] for ch in word.lower()])

word = "Legend"
print(word_to_num(word))
