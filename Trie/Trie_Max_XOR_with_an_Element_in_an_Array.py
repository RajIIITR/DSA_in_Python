class TrieNode:
    def __init__(self):
        self.children = [None] * 2  # Fixed typo from 'choldren' to 'children'

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

    def getMaxXOR(self, num):
        curr = self.root
        mx = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if curr.children[1 - bit] is not None:
                mx |= (1 << i)
                curr = curr.children[1 - bit]
            elif curr.children[bit] is not None:
                curr = curr.children[bit]
            else:
                return -1  # No elements in Trie
        return mx

def maxXorQueries(arr, queries):
    trie = Trie()
    arr.sort()

    indexed_queries = [(Ai, Xi, idx) for idx, (Xi, Ai) in enumerate(queries)]
    indexed_queries.sort()

    result = [0] * len(queries)
    i = 0  # pointer for arr

    for Ai, Xi, idx in indexed_queries:
        while i < len(arr) and arr[i] <= Ai:
            trie.insert(arr[i])
            i += 1
        result[idx] = trie.getMaxXOR(Xi)

    return result

if __name__ == '__main__':
    arr = [3, 2, 4, 8]
    queries = [[4, 5], [1, 3], [4, 8]]
    print(maxXorQueries(arr, queries))  # Output: [7, 3, 12]