# Design Word Search Data Structure Solution
#
# This solution implements an efficient algorithm for the design word search data structure problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class TrieNode:
    def __init__(self):
        self.children = {}
        self. word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """Method: addWord"""
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        """Method: search"""
        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            
            return cur.word
        return dfs(0, self.root)

