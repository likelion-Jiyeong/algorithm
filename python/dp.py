from functools import lru_cache
"""
기본 dynamic programming에 대해서 문제를 풀어보자

"""
# 피보나치 수열 (Top-Down 방식)
memo = [False] * (10+1)
def fib(n):
    if n <= 1:
        return n
    
    if memo[n]:
        return memo[n]
    else:
        return fib(n-1) + fib(n-2)
result = fib(10)
print(f"result > {result}")


# 계단 오르기
@lru_cache(None)
def stairs(n):
    if n == 0 or n == 1:
        return 1
    return stairs(n-1) + stairs(n-2)

result = stairs(4)
print(f"result > {result}")


# 거스름돈 동전 교환

def change_coins(coins, amount):
    INF = float('inf')
    
    @lru_cache(None)
    def dfs(rem):
        if rem == 0:
            return 0
        if rem < 0:
            return INF
    
        best = INF
        for c in coins:
            cnt = dfs(rem - c) + 1
            if cnt < best:
                best = cnt
        return best
    
    res = dfs(amount)
    return -1 if res == INF else res

coins = [1, 2, 5]
amount = 11
result = change_coins(coins, amount)
print(f"result >> {result}")


# 2차원 그리드 최단 경로 개수
def unique_paths(m, n):
    dp = [[0] * n for _ in range(m)]
    # 초기값 (이동할 수 없는 곳)
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    
    """
    dp[1][1] = dp[0][1]+dp[1][0]
    """
    # DP 채우기
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

unique_paths(3, 3)

# dfs 활용
def unique_paths(m, n):
    dp = [[-1] * n for _ in range(m)]

    def dfs(i, j):
        if i==0 or j ==0:
            return 1
        if dp[i][j] != -1: # 이미 계산된 값이 존재하면
            return dp[i][j]
        
        dp[i][j] = dfs(i-1, j) + dfs(i, j-1)
        return dp[i][j]
    return dfs(m-1, n-1)

answer = unique_paths(3, 3)
print(f"answer >> {answer}")


# 최대 연속 합
"""
bottom-top이 편하다
top-bottom이라면 최대값 INF 적용해놓고
모든 배열의 합이 
"""
def max_continious_sum(nums):
    n = len(nums)
    memo = [None] * n # i까지 끝나는 연속합의 최대값

    def dfs(i):
        if memo[i] is not None:
            return memo[i]

        # 기저 사례 : 맨 처음 원소 하나로만 이뤄진 구간
        if i == 0:
            memo[i] = nums[0]
        else:
            memo[i] = max(dfs(i-1)+nums[i], nums[i])
        return memo[i]
    
    best = nums[0]
    for i in range(n):
        best = max(best, dfs(i))
    return best

nums = [-2,1,-3,4,-1,2,1,-5,4]
answer = max_continious_sum(nums)
print(f"answer >> {answer}")
