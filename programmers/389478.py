"""
입력: 총 n개, 가로 w, 찾아야하는 박스 번호
출력: 같은 열에 총 몇개를 더 꺼내야 하는지?
        22, 21, 20, 19
13, 14, 15, 16, 17, 18
12, 11, 10, 9,  8 , 7
1,  2,  3,  4,  5,  6


h = n / 6 + 1
8을 찾으려면..?
몇 번째 층의 몇번째 칸인지를 찾아야 한다
8 / 6 = 
저 이차원 스택을 직접 만들고 나서 해당 모든 리스트에서 같은 
딕셔너리가 아니라 이차원 리스트로 만들수는 없을까?
"""
def solution(n, w, k):
    h = n // w + 1
    result = []
    
    num = 1
    for i in range(h):
        row = []
        for _ in range(w):
            if num > n:
                break
            row.append(num)
            num += 1
        if i % 2 != 0:
            row.sort(reverse=True)
            result.append(row)
        else:
            result.append(row)
    
    # target이 몇 번째 행에 위치하는지 찾기
    row_idx = (k-1) // w
    target_row = result[row_idx]
    target_index = target_row.index(k)

    answer = []
    for idx, i in enumerate(result):
        if len(i) < w:        
            if idx % 2 == 0:
                for _ in range(w - len(i)):
                    i.append(0)
            else:
                for _ in range(w - len(i)):
                    i.insert(0, 0)
        answer.append(i[target_index])
    answer = [i for i in answer if i >= k]
    return len(answer)

n, w, num = 13, 3, 6
answer = solution(n, w, num)
print(f"answer >> {answer}")
