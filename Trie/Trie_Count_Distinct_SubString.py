'''
Given a string 'S', you are supposed to return the number of distinct substrings(including empty substring) 
of the given string. You should implement the program using a trie.
'''


class TrieNode:

    def __init__(self):
        self.children = [None] * 26

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        count = 0
        curr = self.root
        for char in key:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
                count += 1
            curr = curr.children[index]
        return count

def distinctSubstrings(s: str) -> int:
    count = 0
    trie = Trie()

    for i in range(len(s)):
        c = trie.insert(s[i:])
        count += c
    
    return count+1

if __name__ == "__main__":
    print(distinctSubstrings("abc"))