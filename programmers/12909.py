"""
입력 : 문자열 ()
출력 : True/False
구현 방법
스택 
(이면 append
)이면 pop
스택에 없으면 True
남아있으면 False

(()
"""
def solution(s):
    stack = [s[0]]
    i = 1

    while i < len(s):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        i += 1
    
    if len(stack) > 0:
        return False
    else:
        return True


s = "))))))))))()"
answer = solution(s)
print(f"answer >> {answer}")