from itertools import combinations
"""
입력 : orders : 사람들이 주문한 메뉴 조합, course : 몇가지 조합에 대한 결과를 구해야하는지 알려주는 리스트
결과 : course에 해당하는 조합 오름차순 정리

활용 로직 및 알고리즘 : 
리스트를 정렬하여 course 만큼 되는지 확인 -- done
각조합에 해당하는게 있는지 확인 -> 문자열로 확인?
모든 orders 조회 후 count하기 * 이 때 count가 2가 되면 더 볼 필요 없음

-> combinations 라이브러리 활용
"""
def solution(orders, course):
    answer = []
    
    for c in course:
        comb_count = {}
        max_order = []
        for o in orders:
            order_comb = combinations(list(o), c)
            for order in order_comb:
                order_comb_string = "".join(sorted(order))
                if order_comb_string not in comb_count:
                    comb_count[order_comb_string] = 1
                else:
                    comb_count[order_comb_string] += 1
        max_order = [k for k, v in comb_count.items() if v >= 2 and v == max(comb_count.values())]
        answer.extend(max_order)
    answer.sort()
    
    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
answer = solution(orders, course)
print(f"answer >> {answer}")