from itertools import combinations
"""
입력 : 릴레이션
아웃풋: 후보키 개수
조건 : 
1) 각 row별로 유니크해야한다.
2) feature 1, 2, 3개로 만들어서 유니크한지 판단
3) 1개씩 발견하고 다 끝나면 유니크한거 제외 하고 2개 피처로 구성 -> 있다면 후보키 -> 없으면 그 다음 2개
2개에서 아예 없다면 해당 컬럼부터 3개로 넘어감
조합을 만들때는 combinations 라이브러리를 활용하는게 나음
"""
def solution(relation):
    features = len(relation[0])
    rows = len(relation)

    f = 1 # 조합 수 
    i = 0 # 조합 인덱스를 위한 포인터
    used_combs = []

    while f <= features : # i가 전체 피처 개수만큼 돌면 종료 
        all_combs = list(combinations(range(features), f)) # f개 조합 전부
        while i < len(all_combs):
            comb = all_combs[i]
            temp = [tuple(row[j] for j in comb) for row in relation]
            if len(set(temp)) == rows: # 유일성 만족
                # 최소성 체크 : 기존 후보키가 현재 comb의 부분집합이면 제외
                is_minimal = True
                for used in used_combs:
                    if set(used).issubset(set(comb)):
                        is_minimal=False
                        break
                if is_minimal:
                    used_combs.append(comb)
            i+= 1
        f += 1 # row를 다 돌면 
        i = 0
    return len(used_combs)

relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]
answer = solution(relation)
print(f"answer >> {answer}")