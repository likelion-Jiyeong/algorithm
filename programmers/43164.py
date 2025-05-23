from collections import deque
"""
BFS로 해결할 수  있는 문제이다.
1) while문 안에서 디큐로 해결하기
"""

def solution(tickets):
    queue = deque()
    result = []
    n = len(tickets)
    queue.append((['ICN'], [False] * n)) # (현재 경로, 티켓 사용 여부)    
    
    tickets.sort()
    
    while queue:
        path, used = queue.popleft()

        if len(path) == n + 1: # 모든 경로를 다 찾은 경우
            return path


        for i in range(n):
            if not used[i] and tickets[i][0] == path[-1]:
                next_path = path + [tickets[i][1]]
                next_used = used[:]
                next_used[i] = True
                queue.append((next_path, next_used))
            
    return sorted(result)[0]

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
answer = solution(tickets)
print(f"answer >> {answer}")