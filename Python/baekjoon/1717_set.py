import sys
from collections import defaultdict

def main():
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    parent = [i for i in range(n + 1)]

    # union find
    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x != y:
            parent[y] = x

    for i in range(m):
        check, a, b = list(map(int, sys.stdin.readline().strip().split()))
        if check == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")
if __name__ == "__main__":
    main()

"""
7 7
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
1 1 1
"""