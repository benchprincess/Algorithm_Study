def solution(x): 
    answer = True
    a = 0
    X = str(x)
    for i in range(len(X)):
        a += int(X[i])
    
    if x % a != 0:
      answer = False
    return answer