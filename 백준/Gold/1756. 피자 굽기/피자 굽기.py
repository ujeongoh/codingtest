if __name__ == "__main__":
    d,n = map(int,input().split())
    oven = list(map(int,input().split()))
    banjuck = list(map(int,input().split()))

    for i in range(1,d):
        oven[i] = min(oven[i-1],oven[i])
    
    cur = 0
    idx = 0
    for i in range(d-1,0,-1):
        if oven[i] < banjuck[cur]: #반죽이 더 크면 오븐에 못넣으니까 패스
            continue
        cur +=1 # 오븐에 반죽 넣으면 반죽 갯수 체크

        if cur >= n : # 주어진 반죽 모두 오븐에 넣은 경우
            idx = i+1 # i =0 부터 해서 +1 처리 해주기
            break
    print(idx)