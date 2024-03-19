def solution(array):
    array.sort()
    length = len(array)
    
    mid = length // 2
    
    if length % 2 == 0:
        mid -= 1
    
    return array[mid]