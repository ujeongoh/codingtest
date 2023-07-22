def solution(places):
    answer = []
    # 상 하 좌 우 , 대각선-좌상 우상 좌하 우하, +1 상 하 좌 우
    dx = [-1, 1, 0, 0, -1, -1, 1, 1, -2, 2, 0, 0]
    dy = [0, 0, -1, 1, -1, 1, -1, 1, 0, 0, -2, 2]
    
    def check(n, x, y):
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and places[n][nx][ny] == 'P':                
                if i < 4:
                    return False
                elif 4 <= i < 8:
                    if not (places[n][nx][y] == 'X' and places[n][x][ny]) == 'X':
                        return False
                    
                elif i >= 8:
                    if not places[n][(x+nx)//2][(y+ny)//2] == 'X':
                        return False
        return True
    
    for n, place in enumerate(places):
        chk = True
        result = 1
        for i, row in enumerate(place):
            for j, seat in enumerate(row):
                if seat == 'P':
                    if not check(n, i, j):
                        chk = False
                        break
            if not chk:
                result = 0
                break         
        answer.append(result)
        
    return answer