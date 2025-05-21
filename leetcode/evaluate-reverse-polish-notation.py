class Solution:
    """
    eval 사용 없이 사칙 연산을 직접 코드에 작성하는게 훨씬 빠르다.
    """
    def evalRPN(self, tokens: list[str]) -> int:
        answer = 0
        stack = []

        for t in range(len(tokens)):
            if tokens[t] not in ['+', '-', '*', '/']:
                stack.append(tokens[t])
            else:
                if len(stack) >= 2:
                    second = stack.pop()
                    first = stack.pop()
                    print(f"second >> {second}")
                    print(f"first >> {first}")
                    result = f"{first}{tokens[t]}{second}"

                    if tokens[t] == '/':
                        stack.append(int(eval(result)))
                    else:
                        stack.append(eval(result))
                
        answer = int(stack[0])
        return answer

solution = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
answer = solution.evalRPN(tokens)
print(f"answer >> {answer}")
        