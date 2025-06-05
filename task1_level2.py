"""Lab9"""
def read_file():
    """gathering data from file"""
    word_num = 0
    word_list = []
    with open("wchain.in", "r", encoding="utf8") as f:
        word_num = f.readline().split("\n")[0]
        word = f.readline().split("\n")[0]
        while word != "":
            word_list.append(word)
            word = f.readline().split("\n")[0]
    return word_num, word_list

def check_words(word : str, wordlist : list, score = 0):
    """check for max game length"""
    _worked = False
    for letter in word:
        if len(list(word)) == 1:
            return 0
        _t = list(word)
        _t.remove(letter)
        new_word = str("".join(_t))
        if new_word in wordlist:
            _worked = True
            _temp = check_words(new_word, wordlist)
            score = max(score, _temp)
    if _worked:
        return score + 1
    else:
        return 0


def algorythm():
    """lab algo"""
    word_num, word_list = read_file()
    max_pts = 0
    for word in word_list:
        max_pts = max(check_words(word, word_list), max_pts)
    with open("wchain.out", "w", encoding="utf8") as f:
        f.write(str(max_pts))

algorythm()