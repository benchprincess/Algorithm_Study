def solution(n):
    # n의 약수를 num = [] 에 저장
    sum = 0
    for i in range (1, n+1):
        if n % i == 0:
            sum += i
        else:
            pass
        
    return sum