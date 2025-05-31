"""
입력 : 맵기 지수, K개 임계값
출력 : 몇 번 해야 조건 만족하는지
구현 방법
sort를 매번 수행하면 시간초과 뜬다. O(nlogn)
매번 전체 정렬 대신 heap을 사용하면 수행시간이 많이 줄어든다
"""
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        if scoville[0] >= K:
            return answer
        
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        
        heapq.heappush(scoville, new_scoville)
        answer += 1
    return -1

scoville = [1, 2, 3, 9, 10, 12]
K = 7
answer = solution(scoville, K)
print(f"answer >> {answer}")