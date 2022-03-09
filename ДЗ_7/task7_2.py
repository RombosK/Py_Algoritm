# 648. Replace Words ###  https://leetcode.com/problems/replace-words/
import collections
from functools import reduce


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        trie = lambda: collections.defaultdict(trie)
        tried = trie()
        for word in dictionary:
            reduce(dict.__getitem__, word, tried).setdefault('end')

        def replace(word):
            curr = tried
            for i, c in enumerate(word):
                if c not in curr:
                    break
                curr = curr[c]
                if 'end' in curr:
                    return word[:i + 1]
            return word

        return ' '.join(map(replace, sentence.split()))
