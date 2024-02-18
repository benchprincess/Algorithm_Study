def solution(s):
    words = s.split(" ")
    modified_words = []
    
    for word in words:
        for i in range(len(word)):
            if i % 2 == 0:
                modified_words.append(word[i].upper())
            elif i % 2 == 1:
                modified_words.append(word[i].lower())
                
        modified_words.append(" ")
        
    
    a = ''.join(modified_words[:-1])
    print(modified_words)
    return a
    
            