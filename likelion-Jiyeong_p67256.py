def solution(numbers, hand):
    answer = []
    left = [1,4,7]
    right = [3,6,9]
    left_now = 0
    right_now = 0
    for i in numbers:
        if i in left:
            answer.append('L')
            left_now = i
        elif i in right:
            answer.append('R')
            right_now = i
        else:           # 가운데 배열일 경우
            if abs(left_now-i) > abs(right_now-i):
                answer.append('R')
            elif abs(left_now-i) < abs(right_now-i):
                answer.append('L')
            else:
                if hand == 'left':
                    answer.append('L')
                else:
                    answer.append('R')
    print(f"answer >> {answer}")
    answer = ''.join(answer)
    return answer