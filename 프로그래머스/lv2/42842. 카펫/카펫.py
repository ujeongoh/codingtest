def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow + 1):     
        # 수가 맞아떨어지지 않는 경우 pass
        if yellow % i != 0:
            continue
            
        # 노란색 세로, 가로 길이    
        yellow_h = i
        yellow_w = yellow // i
        
        # 추정한 노란 격자 수에 따른 갈색 격자 수 
        brown_cnt = (yellow_h * 2) + (yellow_w * 2) + 4
        
        # 추정 갈색 격자 수와 실제 갈색 격자 수가 일치할 경우 break하고 결과 리턴
        if brown_cnt == brown:
            answer = [yellow_w + 2, yellow_h + 2]
            break
            
    return answer