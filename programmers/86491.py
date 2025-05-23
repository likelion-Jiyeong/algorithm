"""
입력 : 가로, 세로 명함 너비 쌍
출력 : 가장 작은 사이즈 지갑 크기
구현 방법
완전탐색 - 모든 경우의 수를 다 해보고 작은 것을 찾아야한다.
dfs 사용? permutations?

-> 단순히 방향을 통일 시켜서 짧게 구현 가능하다.


"""
def solution(sizes):

    xds = []
    yds = []

    for w, h in sizes:
        xds.append(max(w,h)) # 긴쪽
        yds.append(min(w,h)) # 짧은 쪽
    answer = max(xds) * max(yds)    
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
answer = solution(sizes)
print(f"answer >> {answer}")