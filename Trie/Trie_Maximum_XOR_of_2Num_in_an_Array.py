'''
You are given two arrays of non-negative integers say 'arr1' and 'arr2'. Your task is to find the maximum value 
of ( 'A' xor 'B' ) where 'A' and 'B' are any elements from 'arr1' and 'arr2' respectively and 'xor' represents 
the bitwise xor operation.
'''


class TrieNode:
    def __init__(self):
        self.children = [None] * 2
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        curr = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if curr.children[bit] is None:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]

def maxXOR(n, m, arr1, arr2):
    trie  = Trie()
    
    for num in arr1:
        trie.insert(num)

    mx = 0
    
    for num in arr2:
        curr = trie.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if curr.children[1 - bit] is not None:
                mx = mx | (1 << i)
                curr = curr.children[1 - bit]
            else:
                curr = curr.children[bit]
    return mx

if __name__ == '__main__':
    # n, m = map(int, input().split())
    # arr1 = list(map(int, input().split()))
    # arr2 = list(map(int, input().split()))

    n, m = 7, 7
    arr1 = [6, 6, 0, 6, 8, 5, 6]
    arr2 = [1, 7, 1, 7, 8, 0, 2]

    print(maxXOR(n, m, arr1, arr2)) #Output: 15