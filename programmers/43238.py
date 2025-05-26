"""
입력 : 입국심사 기다리는 사람 수 n, 각 심사관이 한 명당 걸리는 시간 리스트
출력 : 최소 걸리는 시간
수행방법
이분탐색 -> 부족하지도 넘치지도 않는 최적의 값을 찾는 문제 -> 설정한 시간동안 n보다 많은 수를 심사했다면 너무 시간이 많은 것이고
n미만의 사람을 심사했다면 시간이 너무 적은 것

"""
def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left+right) // 2
        people = 0
        for time in times:
            people += mid //time
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer


n = 6
times = [7, 10]
answer = solution(n, times)
print(f"answer >> {answer}")