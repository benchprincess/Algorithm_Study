def solution(food):
    answer = ''
    list = ''
    
    fn = 0
    for i in food:
        if i <2:
            pass
        else:
            for add in range(i//2):
                list += str(fn)
        fn += 1
        
    answer = list + '0' + list[::-1]
    return answer
  