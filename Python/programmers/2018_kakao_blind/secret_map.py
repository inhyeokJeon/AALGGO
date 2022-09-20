def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(bin(arr1[i] | arr2[i])[2:].
                      zfill(n).
                      replace('0', ' ').
                      replace('1', '#'))
    return answer

n = 5
arr1 =[9, 20, 28, 18, 11]
arr2 =[30, 1, 21, 17, 28]
# exp ["#####","# # #", "### #", "# ##", "#####"]
print(solution(n, arr1, arr2))