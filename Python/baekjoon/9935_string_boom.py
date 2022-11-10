import sys

def main():
    string = sys.stdin.readline().strip()
    booms = sys.stdin.readline().strip()
    # string = "mirokrroovC"
    # booms = "ro"

    length = len(booms)
    result = []
    def boom(ss):
        for _ in range(length):
            ss.pop()

    for s in string:
        result.append(s)
        if booms in ''.join(result[len(result) - length:]):
            boom(result)

    if result:
        print(''.join(result))
    else:
        print("FRULA")



if __name__ == "__main__":
    main()

"""inputs
mirkovC4nizCC44
C4
"""