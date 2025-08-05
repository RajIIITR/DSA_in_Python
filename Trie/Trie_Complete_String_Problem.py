'''
A string is called a complete string if every prefix of this string is also present in the array 'A'. 
Ninja is challenged to find the longest complete string in the array ‘A’.If there are multiple strings with 
the same length, return the lexicographically smallest one and if no string exists, return "None".
'''


from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

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
        curr.isLeaf = True

    def isCompleteString(self, key):
        curr = self.root
        for char in key:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
            if not curr.isLeaf:
                return False
        return True 
    
def completeString(n: int, a: List[str]) -> str:
    trie = Trie()
    for word in a:
        trie.insert(word)
    
    longest = ""
    for word in a:
        if trie.isCompleteString(word):
            if len(word) > len(longest):
                longest = word 
            elif len(word) == len(longest) and word < longest:
                longest = word

    return longest if longest else "None"

if __name__ == '__main__':
    a = ["n", "ni", "nin", "ninj", "ninja", "ninga"]
    print(completeString(len(a), a))  # Output: "ninja"
