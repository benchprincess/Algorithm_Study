def solution(d, budget):
    count = 0
    d.sort()
    for cost in d:
        budget -= cost
        if budget < 0:
            break
        count += 1
    return count
