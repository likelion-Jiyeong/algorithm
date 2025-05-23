from itertools import permutations
"""
모든 경우의 수 진행하기
순열, 조합 -> permutations
가능한 수 반환

!온전히 풀기 ok
"""
def solution(k, dungeons):
    answer = -1
    combs = list(permutations(dungeons))
    
    for comb in combs:
        blood = k
        cnt = 0
        for i in list(comb):
            if i[0] <= blood:
                blood -= i[1]
                cnt += 1
        answer = max(cnt, answer)

    print(f"answer >> {answer}")

    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]
answer = solution(k, dungeons)