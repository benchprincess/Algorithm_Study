def solution(rsp):
    # 손동작을 이기는 규칙을 딕셔너리로 정의
    win = {'2': '0', '0': '5', '5': '2'}
    # 각 문자에 대해 이기는 손동작으로 변환
    result = ''.join(win[char] for char in rsp)
    return result