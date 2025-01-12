def solution(n):
    N = str(n)
    sum = 0
    for i in range(0, len(N)):
        sum += int(N[i])
    return sum