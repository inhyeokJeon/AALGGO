# https://www.acmicpc.net/problem/1967
# no same element
import sys
sys.setrecursionlimit(10 ** 9)
def main():
    stack = []
    while True:
        try:
            n = int(sys.stdin.readline().strip())
            stack.append(n)
        except:
            break


    def solve(left, right):
        if left > right:
            return

        mid = right + 1
        for i in range(left + 1, right + 1):
            if stack[i] > stack[left]:
                mid = i
                break
        solve(left + 1, mid - 1)
        solve(mid, right)
        print(stack[left])

    solve(0, len(stack) - 1)

if __name__ == "__main__":
    main()
