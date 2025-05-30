from collections import Counter
"""
입력 : 사람 리스트, 서로 주고 받은 기록
출력 : 가장 많이 받은 사람이 받은 선물 수
조건 : 두 사람이 주고 받은 기록이 있다면 더 많이 선물을 준 사람이 하나를 받는다.
주고 받은 기록 없거나 같으면 선물지수가 더 큰사람이 더 작은 사람에게 하나 받는다.
선물지수는 친구들에게 준 선물수 - 받은 선물 수
선물지수도 같다면 다음달에 선물 주고 받지 않음

딕셔너리에 준사람 : 받는 사람, count 저장해놓기
선물지수도 

혹은 counter 활용하기?


방법
일단 직접 구현하기
for friends 돌고, gifts 돌아서 각 사람별로 조건 타서 몇 개 받는지 저장해야한다
결과 : 각 사람별로 몇 개를 받는지 저장해놔야한다
"""
def solution(friends, gifts):
    logs = [tuple(x.split()) for x in gifts]
    counter = Counter(logs)
    result = {i: 0 for i in friends}

    give_gift_idx = {f: 0 for f in friends}
    get_gift_idx = {f: 0 for f in friends}
    # 선물 지수 미리 저장해두기
    for l in logs:
        give_gift_idx[l[0]] += 1

    for l in logs:
        get_gift_idx[l[1]] += 1

    for i_idx, i in enumerate(friends):
        for j_idx, j in enumerate(friends):
            if i_idx >= j_idx: # 쌍 중복 방지
                continue

            ab = counter[(i, j)]
            ba = counter[(j, i)]

            if ab > ba:
                result[i] += 1
            elif ab < ba:
                result[j] += 1
            else: # 같으면 선물 지수 비교
                score_i = give_gift_idx[i] - get_gift_idx[i]
                score_j = give_gift_idx[j] - get_gift_idx[j]

                if score_i > score_j:
                    result[i] += 1
                elif score_i < score_j:
                    result[j] += 1
                else:
                    pass
                print(result)

    return max(result.values())

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

answer = solution(friends, gifts)
print(f"answer >> {answer}")