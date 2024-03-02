def solution(hp):
    general = 5
    soldier = 3
    ergate = 1
    
    num_general = hp // general
    remain_hp = hp % general
    
    num_soldier = remain_hp // soldier
    remain_hp %= soldier
    
    answer = num_general + num_soldier + remain_hp
    return answer