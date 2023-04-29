import sys
input = sys.stdin.readline

if __name__ == "__main__":

    # 세로선 i가 사다리 타고 난 후 결과값이 i이면 true를 반환 
    def check():
        for i in range(1, n + 1):
            cur = i
            for j in range(1, h + 1):
                if ladder[j][cur] == 1: #
                    cur += 1
                elif ladder[j][cur-1] == 1:
                    cur -= 1
            if cur != i:
                return False
        return True

    def dfs(cnt,x):
        global answer
        if check():
            answer = min(answer, cnt)
            return
        if answer <= cnt or cnt == 3:
            return        
        for i in range(x, h+1):
            for j in range(1, n):
                if ladder[i][j] == 0 and ladder[i][j-1] == 0 and ladder[i][j+1] == 0: 
                    ladder[i][j] = 1
                    dfs(cnt+1, i)
                    ladder[i][j] = 0 

    n,m,h = map(int,input().split())
    ladder = [[0] * (n + 1) for _ in range(h + 1)]

    for _ in range(m):
        a, b = map(int,input().split())
        ladder[a][b] = 1

    answer = 4
    dfs(0,1)

    print(answer if answer < 4 else -1)