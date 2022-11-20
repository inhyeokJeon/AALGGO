# https://www.acmicpc.net/problem/1967
import sys
from collections import defaultdict, deque


def main():
    n = int(sys.stdin.readline().strip())
    graph = defaultdict(dict)
    for _ in range(n):
        node, left, right = sys.stdin.readline().strip().split()
        graph[node]["L"] = left
        graph[node]["R"] = right

    def preorder(start):
        if start == ".":
            return
        print(start, end="")
        for next in graph[start]:
            preorder(graph[start][next])

    def inorder(start):
        if start == ".":
            return
        left = graph[start]["L"]
        right = graph[start]["R"]
        inorder(left)
        print(start, end= "")
        inorder(right)

    def postorder(start):
        if start == ".":
            return
        for next in graph[start]:
            postorder(graph[start][next])
        print(start, end="")
    preorder("A")
    print()
    inorder("A")
    print()
    postorder("A")
if __name__ == "__main__":
    main()
