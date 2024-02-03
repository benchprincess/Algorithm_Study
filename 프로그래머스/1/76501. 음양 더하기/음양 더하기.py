def solution(absolutes, signs):
    answer = 0
    for i, s in enumerate(signs):
        if s:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer