from itertools import product
"""
입력 : word 'A, E, I, O, U'
출력 : word가 몇번째에 위치하는가
수행방법
itertools의 product 라이브러리 활용하기
"""
def solution(word):
    strs = ['A', 'E', 'I', 'O', 'U']
    result = []

    for i in range(5):
        for v in product(strs, repeat=i+1):
            result.append(''.join(v))
    result.sort()
    return result.index(word) + 1

# dfs 활용
def solution(word):
    words = 'AEIOU'
    dict = []

    def dfs(cnt, w):
        # 최대 길이는 5
        if cnt == 5:
            return
        for i in range(len(words)):
            dict.append(w+words[i])
            dfs(cnt+1, w+words[i])
    
    dfs(0, '')
    return dict.index(word) + 1



word = "I"
answer = solution(word)
print(f"answer >> {answer}")

# 재귀함수 구현해보기
"""
5+4+recursive_sum(3)
5+4+3+recursive_sum(2)
5+4+3+2+recursive_sum(1)
"""

def recursive_sum(n):
    if n==1:
        return 1
    return n + recursive_sum(n-1)

recursive_sum(5) # 5+recursive_sum(4)

# 문자열 뒤집기
def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:])+s[0]

reverse_string("cat") #t + a-> at + c

# 트리 구조

tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}
result = []
def dfs(node):
    result.append(node)
    for child in tree[node]:
        dfs(child)

dfs('A')
print(f"result >> {result}")

# 총 노드 개수 세기
def count_nodes(node):
    count = 1
    for child in tree[node]:
        count += count_nodes(child)
    return count

print(count_nodes('A'))

tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}

# 특정 노드까지의 경로 출력
print("특정 노드까지의 경로 출력")
def find_path(start, end):
    path = []
    
    def dfs(node):
        path.append(node)
        print(f"Enter {node}, path: {path}")

        if node == end:
            print(f"Found target: {path}")
            return True
        
        for child in tree[node]:
            if dfs(child):
                return True
        path.pop() # 백트래킹: 경로 아님 -> 되돌아가
        print(f"Backtrack from {node}, path: {path}")
        return False
    dfs(start)
    return path 

print(find_path('A', 'F'))
