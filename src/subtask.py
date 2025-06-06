"""search for a user"""
from task1_level3 import create_trie, TheTrieItself

def find_user(users = [["heck", "man"],["justterrible", "heck"]], anon = ["heck","justterrible","awful"]):
    trie = create_trie(anon)
    percentage = []
    for el in users:
        percentage.append([0])
    for user in users:
        _idx = users.index(user)
        for word in user:
            if trie.find(word):
                percentage[_idx][0] += 1
    for perc in percentage:
        perc[0] = perc[0] / len(users[percentage.index(perc)]) * 100
    print(percentage)

find_user()
