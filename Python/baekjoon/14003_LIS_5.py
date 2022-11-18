import sys
def main():
    n = int(sys.stdin.readline().strip())

    sequence = list(map(int,sys.stdin.readline().strip().split()))
    if n == 1:
        print(1)
        print(sequence[0])
        return
    temp = [-1000000001]
    cands = [[] for _ in range(n + 1)]
    for i in range(n):
        if sequence[i] > temp[-1]:
            cands[len(temp)].append((sequence[i], i))
            temp.append(sequence[i])
        else:
            left = 1
            right = len(temp) - 1
            while left <= right:
                mid = (left + right) // 2
                if temp[mid] < sequence[i]:
                    left = mid + 1
                else:
                    right = mid - 1

            temp[left] = sequence[i]
            cands[left].append((sequence[i], i))
    len_result = len(temp) - 1

    if len_result == 1:
        print(len_result)
        print(sequence[0])
        return
    # print(cands)

    cands = cands[1:len_result + 1]
    max_val, max_idx = cands.pop()[0]
    ret = [max_val]
    for cand in reversed(cands):
        cand.sort(reverse= True, key = lambda x : x[1])
        for val, idx in cand:
            if idx < max_idx and val < max_val:
                ret.append(val)
                max_idx = idx
                max_val = val
                break

    print(len_result)
    print(*reversed(ret))

if __name__ == "__main__":
    main()

"""
7
3 1 5 2 3 6 4
"""

"""
8
30 1 9 40 7 5 4 90
"""