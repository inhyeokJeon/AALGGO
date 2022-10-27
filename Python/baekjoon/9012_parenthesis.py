import sys

def check(string):
    stack = []
    for s in string:
        if s == "(":
            stack.append(")")
        elif s == "[":
            stack.append("]")
        elif s == ")" or s == "]":
            if stack:
                char = stack.pop()
                if char != s:
                    return False
            else:
                return False
    if stack:
        return False
    return True

def solution():
    while True:
        strings = sys.stdin.readline().split(".")
        if strings[0]:
            if check(strings[0]):
                print("yes")
            else:
                print("no")
        else:
            break
solution()


