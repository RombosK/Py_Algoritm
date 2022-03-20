# 211. Design Add and Search Words Data Structure  https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_string = False
        self.words = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for sym in word:
            if not sym in curr.words:
                curr.words[sym] = TrieNode()
            curr = curr.words[sym]
        curr.is_string = True

    def search(self, word):
        return self.helper(word, 0, self.root)

    def helper(self, word, start, curr):
        if start == len(word):
            return curr.is_string
        if word[start] in curr.words:
            return self.helper(word, start + 1, curr.words[word[start]])
        elif word[start] == '.':
            for c in curr.words:
                if self.helper(word, start + 1, curr.words[c]):
                    return True

        return False
