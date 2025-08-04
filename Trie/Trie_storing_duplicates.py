class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.cntEndsWith = 0
        self.cntPrefix = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        curr = self.root
        for char in key:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.cntPrefix += 1
        curr.cntEndsWith += 1

    def countWordsEqualTo(self, key):
        curr = self.root
        for char in key:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return 0
            curr = curr.children[index]
        return curr.cntEndsWith
    
    def countWordsStartingWith(self, key):
        curr = self.root
        for char in key:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return 0
            curr = curr.children[index]
        return curr.cntPrefix

    def erase(self, key):
        curr = self.root
        for char in key:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                raise ValueError("Key not found")
            curr = curr.children[index]
            curr.cntPrefix -= 1
        if curr.cntEndsWith > 0:
            curr.cntEndsWith -= 1
        else:
            raise ValueError("Key not found")


if __name__ == '__main__':
    trie = Trie()
    arr = ["and", "ant", "ant", "apple"]
    for s in arr:
        trie.insert(s)

    print(trie.countWordsEqualTo("ant"))
    print(trie.countWordsStartingWith("an"))
    trie.erase("ant")
    print(trie.countWordsEqualTo("ant"))
    print(trie.countWordsStartingWith("an"))  
    # trie.erase("a")   # It will throw an error as when we are erasing we are keeping in mind the entire word is deleted not a single character/prefix
    trie.erase("apples")