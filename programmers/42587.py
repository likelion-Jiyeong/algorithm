"""
입력 : 우선순위가 담긴 배열
출력 : location번째가 몇 번째로 수행되는가
수행방법
id, priorities 매핑을 만든다
deque를 활용해서 가장 왼쪽에 뽑은게 
deque에서 max를 계산한다
max값이면 answer에 저장한다
이 때 location 값도 같이 저장한다
만약에 max보다 작으면 queue에 append한다

최종으로 나온 answer에 숫자로 2, 3, 0, 1 저장 되면 idx를 반환한다
"""
from collections import deque
def solution(priorities, location):
    answer = []
    queue = deque(((i, priorities[i]) for i in range(len(priorities))))
    
    while queue:
        
        curr, priority = queue.popleft()
        if any(priority < prior for _, prior in queue): 
            queue.append((curr, priority))
        else:               
            answer.append(curr)
    return answer.index(location) + 1

priorities = [2, 1, 3, 2]
location = 2
answer = solution(priorities, location)
print(f"answer >> {answer}")