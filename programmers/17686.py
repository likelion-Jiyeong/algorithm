"""
입력 : 파일명 (head, number, tail로 구성)
1) head 사전순으로 정렬 (대소문자 구분 ㄴ)
2) number로 정렬 (숫자 순으로 정렬된다)
3) 다 같으면 원래 index 순으로 정렬
구현방법
head, number, tail로 나눠야한다?
for문으로 숫자가 나오기 전까지 추출하기
숫자가 나왔을 때부터 숫자가 아닐때까지 추출하기

"""
def solution(files):
    answer = []
    temp = []

    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                tail = '' # 없으면 런타임 에러 발생

                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                temp.append([head, number, tail])
                head, number, tail = '', '', ''
                break
    temp = sorted(temp, key=lambda x:(x[0].lower(), int(x[1])))
    print(temp)
    answer = [''.join(i) for i in temp]

    return answer

files = ["file00.txt1", "file0.txt1", "file0000000.txt1"]
answer = solution(files)
print(answer)