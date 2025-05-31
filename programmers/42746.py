"""
입력 : 정수가 주어졌을 때 이어서 만들 수 있는 가장 큰 수를 나타내라
출력 : 가장 큰 수를 나타내야한다.
구현 방법
953
첫번째 자리수 비교하고 3두번째 자리수 비교
9534330
"""
def solution(numbers):
    answer = 0
    
    result = list(map(str, numbers))
    result.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(result)

    return str(int(answer))

numbers = [3, 30, 34, 5, 9]
answer = solution(numbers)
print(f"answer >> {answer}")
