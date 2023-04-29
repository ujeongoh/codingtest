import sys
input = sys.stdin.readline

if __name__ == "__main__":

    # 세로선 i가 사다리 타고 난 후 결과값이 i이면 true를 반환 
    def check():
        is_valid = True
        for i in range(1, n + 1):
            cur = i
            for j in range(1, h + 1):
                if ladder[j][cur] == 1:
                    cur += 1
                elif ladder[j][cur-1] == 1:
                    cur -= 1
            if cur != i:
                is_valid = False
                break
        return is_valid

    def dfs(cnt, x, y):
        global ans
        if check(): # 현재 상태에서 각 출발점이 도착점으로 잘 도착하는지 확인
            ans = min(ans, cnt)
            return
        elif cnt == 3 or ans <= cnt: # 도착점이 정상적이지 않으면
            # cnt 값이 3일 경우 그 다음 호출에서 cnt가 4가 되어 문제 조건 위반하므로 return
            # cnt 값이 ans 보다 크거나 같을 경우에는 그 다음 경우를 볼 필요가 없으므로 return
            return
        # 행
        for i in range(x, h+1):
            # 가로선을 우선으로 탐색하므로
            if i == x: k = y # 행이 변경되기 전에는 가로선을 계속해서 탐색
            else: k = 0 # 행이 변경될 경우 가로선 처음부터 탐색
            for j in range(k, n): # 세로선(열)
                if not ladder[i][j] and not ladder[i][j + 1]: # 가로선을 놨을 때 오른쪽에 -가 존재하지 않는 경우
                    if j > 0 and ladder[i][j - 1]: 
                        continue # 가로선을 놨을 때 왼쪽에 -가 존재할 경우 continue (--가 되면 안되기 때문)
                    ladder[i][j] = True # 가로선 놓기
                    dfs(cnt + 1, i, j + 2) # cnt 1 증가, 세로선 그대로, -- 이 되면 안되므로 가로선은 2증가
                    ladder[i][j] = False # 가로선 없애기


    n,m,h = map(int,input().split())
    ladder = [[0] * (n + 1) for _ in range(h + 1)]

    for _ in range(m):
        a, b = map(int,input().split())
        ladder[a][b] = 1

    ans = 4
    dfs(0, 1, 1)

    print(ans if ans < 4 else -1)
