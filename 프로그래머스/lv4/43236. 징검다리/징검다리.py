def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left, right = 1, distance

    while left <= right:
        del_rock_cnt = 0
        rock_mid = 0
        target = (left + right) // 2

        for rock in rocks:
            if rock - rock_mid < target:
                del_rock_cnt += 1
            else:
                rock_mid = rock

        if del_rock_cnt > n:
            right = target - 1
        else:
            left = target + 1
            answer = target

    return answer