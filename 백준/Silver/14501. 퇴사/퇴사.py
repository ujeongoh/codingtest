import sys

def dfs(day, price_cnt):
    global answer

    # 퇴사일이면 answer 계산
    if day == n:
        answer = max(answer, price_cnt)
        #print(f'최종가격 : {price_cnt}')
        return
    
    if day + time_price[day][0] <= n :
        #print(f'{day+1}일에 상담 받음, 현재 { price_cnt + time_price[day][1]}원')
        dfs(day + time_price[day][0], price_cnt + time_price[day][1])

    #print(f'{day+1}일에 상담 안 받음, 현재 {price_cnt}원')
    dfs(day + 1, price_cnt)



n = int(input())
time_price = { i : list(map(int,input().split())) for i in range(n) }
answer = 0
dfs(0, 0)
print(answer)

        

