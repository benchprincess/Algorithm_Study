def solution(num_list):
    even = sum(1 for num in num_list if num %2 == 0)
    odd = len(num_list) - even
    return [even, odd]