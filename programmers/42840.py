"""
입력: 정답리스트 (문제 수와 동일)
출력: 3명중 가장 많이 맞힌 사람, 동일 하면 오름차순
1번 : [1,2,3,4,5]
2번 : [2,1,2,3,2,4,2,5]
3번 : [3,3,1,1,2,2,4,4,5,5]
해결방법
3명 다 진행해보고 정답이 몇 개인 지 맞히는 문제
1번은 answer과 같은게 몇 개인지 확인
2번은 answer이 2번과 같은게 몇 개인지 확인
3번은 몇개인지 확인
예를 들어 1,2,3,4,5,5,5,5,5가 정답이라면?
정답개수를 1번 개수만큼 잘라서 i가 one poinrter 구성?
answer[0:5], answer[6:]
비교할때는 for문 

"""
def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    students = [first, second, third]
    
    idx = 0
    for s in students:
        cnt = 0
        for i in range(0, len(answers), len(s)):
            for j in range(len(answers[i:len(s) + i])):
                if s[j] == answers[i + j]:
                    cnt += 1
        idx += 1
        answer.append((idx, cnt))
    
    sorted_answer = sorted(answer, key=lambda x: (-x[1], x[0]))
    max_value = sorted_answer[0][1]
    top_students = [a for a, cnt in sorted_answer if cnt == max_value]
    if len(top_students) == 1:
        return top_students
    else:
        top_students.sort()
        return top_students
        

answers = [1,3,2,4,2]
answer = solution(answers)
print(f"answer >> {answer}")