"""
입력 : 트라이앵글
출력 : 바닥까지 갈까 거처간 숫자의 합이 가장 큰 경우 반환
구현 방법
dp, top-down방식
"""
def solution(triangle):

    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0: #왼쪽 끝이면
                triangle[i][j] += triangle[i-1][j]
            elif j == i: #오른쪽 끝이면
                triangle[i][j] += triangle[i-1][j-1]
            else: #가운데라면
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])


# dfs 활용 방법
def solution(triangle):
    n = len(triangle)

    memo = [[None] * n for _ in range(n)]
    print(memo)
    def dfs(i, j):
        if memo[i][j] is not None:
            return memo[i][j]
        
        if i == n-1:
            return triangle[i][j]
        
        left = dfs(i+1, j)
        right = dfs(i+1, j+1)

        memo[i][j] = triangle[i][j] + max(left, right)
        return memo[i][j]
    
    return dfs(0,0)
    
        
        


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
answer = solution(triangle)
print(answer)

