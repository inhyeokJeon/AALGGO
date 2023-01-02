import sys

def main():
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    parent = [0] * n
    for i in range(n):
        parent[i] = i
    result = 0
    # union find
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x != y:
            parent[y] = x
    for i in range(1, m + 1):
        f1, f2 = list(map(int, sys.stdin.readline().strip().split()))
        if find(f1) == find(f2):
            return i

        if f1 < f2:
            union(f1, f2)
        else:
            union(f2, f1)
    return result

if __name__ == "__main__":
    print(main())

"""
6 5
0 1
1 2
2 3
5 4
0 4
"""