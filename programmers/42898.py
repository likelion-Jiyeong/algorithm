"""
입력 : 좌표 m, n
puddles 물웅덩이 좌표 해당 부분은 피해서 가야한다.
출력
최단 경로 구하기

DP 적용
memo로 길 저장하기
"""
def solution(m, n, puddles):

    puddles = set((x, y) for x, y in puddles)
    print(puddles)

    memo = [[-1] * (n+1) for _ in range(m+1)]

    def dfs(x, y):
        if x > m or y > n or (x, y) in puddles:
            return 0
        if x == m and y == n: # 도착지에 도달했을 경우
            return 1
        if memo[x][y] > -1:
            return memo[x][y]
        
        memo[x][y] = dfs(x+1, y) + dfs(x, y+1)
        return memo[x][y]

    return dfs(1,1)

m, n = 4, 3
puddles = [[2, 2]]
answer = solution(m, n, puddles)
print(f"answer >> {answer}")