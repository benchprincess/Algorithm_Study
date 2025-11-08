def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        day = (100 - p + s - 1) // s
        days.append(day)
    
    result = []
    while days:
        current = days.pop(0)  # ← 여기서 O(n) 발생!
        count = 1
        while days and days[0] <= current:
            days.pop(0)
            count += 1
        result.append(count)
    return result
