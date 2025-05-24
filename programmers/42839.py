from itertools import permutations
"""
입력 : 숫자가 적힌 문자열 0-9
출력 : 소수개수
진행 방법:
숫자로 모든 조합을 만든다.
소수인지 판별한다. 소수는 n/ 2

모든 combs를 생성해야한다.
1, 7 -> 
"""

def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    combs = []

    for i in range(1, len(numbers)+1):
        combs.extend(list(set(permutations(numbers, i))))

    combs_str = [''.join(i) for i in combs]
    print(f"combs_str >> {combs_str}")

    for c in combs_str:
        if c.startswith('0'):
            pass
        else:
            is_prime = isPrime(int(c))
            if is_prime:
                print(f"c >> {c}")
                answer += 1

    return answer



numbers = "17"
answer = solution(numbers)
print(f"answer >> {answer}")