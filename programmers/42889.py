"""
입력 : stages 개수, 이용자가 멈춰있는 스테이지 번호
출력 : 실패율이 높은 스테이지 순으로 내림차순
조건 : 도달한 유저가 없으면 실패율 0, 
스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 순

8명 중 1개의 스테이지 이므로 
1: 1 / 8 -> 0.16
2: 3/ 7 -> 0.2x
3: 2 / 4 -> 0.5
4: 1/2 -> 0.5
5: 0/1 -> 0

스테이지별로  실패율을 저장해야한다
3, 4, 2, 1, 5

0 : 0
1 : 0
2 : 0
3 : 0
4 : 1

for문 stages
"""
from collections import Counter

def solution(N, stages):
    answer = []
    stage_fail = {}
    for i in range(1, N+1):
        stage_fail[i] = 0

    stage_fail = {i: 0 for i in range(1, N+1)}

    counter = Counter(stages)
    total = len(stages)

    for i in range(1, N+1):
        if total > 0:
            stage_fail[i] = counter[i] / total
            total -= counter[i]
        else:
            stage_fail[i] = 0
    answer = sorted(stage_fail.items(), key=lambda x: (-x[1], x[0]))

    return [key for key, value in answer]

N = 4
stages = [4,4,4,4,4]
answer = solution(N, stages)
print(f"answer >> {answer}")