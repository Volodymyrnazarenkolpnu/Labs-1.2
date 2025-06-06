"""lab7, task1, level3, variant3, """

class TrieNode():
    """Node of trie"""
    def __init__(self):
        self.children = [None] * 26

        self.leaf = False

class TheTrieItself():
    """the trie itself"""
    def __init__(self):
        self.root = TrieNode()

    def push(self, word):
        """add a word to the trie"""
        current = self.root
        for l in word:
            _idx = ord(l) - ord("a")
            if current.children[_idx] is None:
                current.children[_idx] = TrieNode()
            current = current.children[_idx]
        current.leaf = True

    def find(self, word):
        """find if a word is in trie"""
        current = self.root
        for l in word:
            _idx = ord(l) - ord("a")
            if current.children[_idx] is None:
                return False
            current = current.children[_idx]
        return current.leaf

    def find_prefix(self, pfix):
        """look for prefix in trie"""
        current = self.root
        for l in pfix:
            _idx = ord(l) - ord("a")
            if current.children[_idx] is None:
                return False
            current = current.children[_idx]
        return True

def create_trie(wordlist):
    """main algo"""
    new_trie = TheTrieItself()
    for word in wordlist:
        new_trie.push(word)
    return new_trie