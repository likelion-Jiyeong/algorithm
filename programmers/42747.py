"""
입력 : 논문 인용 수 리스트
출력 : h-index
조건
n편 중 h번 이상 인용된 논문이 h편 이상, 나머지 논문이 h번 이하라면 h의 최대값이 이 과학자의 h-index
예를 들어 5개중에 h 1 개씩 이상 4편 이상, 1편이 1번 이하라면 ok
5개중에 h 2일 경우
3개, 나머지가 2번 이하 0, 1 ok

h 3일 경우
3개, 나머지가 3번 이하 0, 1

h 4일 경우
2개 - 실패

가장 많은 수가 h - index라고 생각하고 하나씩 줄여나간다?
h가 6인 경우 
"""
def solution(citations):
    citations.sort()
    max_h = max(citations)

    n = len(citations)
    for h in range(max_h, 0, -1):
        over = [c for c in citations if c >= h]
        if len(over) >= h:
            # 작은 경우도 판단
            if h >= n - len(over): # h_index
                return h
    return 0


citations = [3, 0, 6, 1, 5]
answer = solution(citations)
print(f"answer >> {answer}")