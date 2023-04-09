def solution(n, times):
    answer = 0
    times.sort()
    left = 1
    right = max(times) * n
    
    while left <= right:
        people_cnt = 0
        mid = (left + right) // 2
        for time in times:
            people_cnt += mid // time

            
        if people_cnt < n:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
    
    return answer