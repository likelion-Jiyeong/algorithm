# 소수 찾기
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i != 0:
            answer += 1
    print(f"answer >> {answer}")
    return answer
solution(10)