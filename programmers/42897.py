"""
입력 : 각 집에 돈이 담긴 배열
출력 : 돈의 최댓값
"""

def method(money, start, end):
    memo = [None] * len(money)

    def dfs(i):
        if i > end:
            return 0
        if memo[i] is not None:
            return memo[i]
        
        steal = memo[i] = money[i] + dfs(i+2)
        skip = dfs(i+1)
        memo[i] = max(steal, skip)
        return memo[i]
    return dfs(start)

def solution(money):

    n = len(money)
    if n == 1:
        return money[0]

    maxA = method(money, 0, n-2)
    maxB = method(money, 1, n-1)
    return max(maxA, maxB)

money = [1, 2, 3, 1]
answer = solution(money)
print(f"answer >> {answer}")