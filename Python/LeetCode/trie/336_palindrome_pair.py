from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.word = -1
        self.children = defaultdict(TrieNode)
        self.palindrome_word = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    def insert(self, word: str, index: int) -> None:
        node = self.root
        for i, w in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word) - i]):
                node.palindrome_word.append(index)
            node = node.children[w]
        node.word = index

    def search(self, word: str, index: int) -> list[list[int]]:
        node = self.root
        result = []
        # word 를 따라 내려갔을 때 중간에 id가 있고 word 가 palindrome 일때
        while word:
            if node.word != -1:
                if self.is_palindrome(word):
                    result.append([index, node.word])
            if word[0] not in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # word ID
        if node.word != -1 and node.word != index:
            result.append([index, node.word])
        # palindrome ID
        for palindrome in node.palindrome_word:
            result.append([index, palindrome])

        return result

    def print_trie(self) -> None:
        # dfs 출력
        node = self.root
        stack = [(node,"")]
        visited = []

        while stack:
            new_node, val = stack.pop()
            if new_node not in visited:
                visited.append(new_node)
                print(val, new_node.word, new_node.palindrome_word)
                for ke in new_node.children.keys():
                    stack.append((new_node.children[ke], ke))

from typing import List


class Solution:
    # brute force -> time limit exceed

    # def palindromePairs(self, words: List[str]) -> List[List[int]]:
    #     length = len(words)
    #     result = []
    #     for i in range(length):
    #         for j in range(length):
    #             if i == j:
    #                 continue
    #             concat = words[i] + words[j]
    #             if concat[:] == concat[::-1]:
    #                 result.append([i, j])
    #     return result

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        result = []
        for idx, word in enumerate(words):
            trie.insert(word, idx)

        # trie.print_trie()
        for idx, word in enumerate(words):
            result.extend(trie.search(word, idx))

        return result

sol = Solution()
print(sol.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
# print(sol.palindromePairs(["a",""]))
