if __name__ == "__main__":
    n,m = map(int,input().split())
    time = [int(input()) for _ in range(n)]
    
    l = min(time)
    r = max(time) * m 

    res = r
    

    while l <= r:
        target = 0
        mid = (l + r) // 2 

        for i in range(n):
            target +=  mid // time[i]

        if target >= m :
            res = min (res,mid)
            r = mid -1
        else :
            l = mid + 1

    print(res)