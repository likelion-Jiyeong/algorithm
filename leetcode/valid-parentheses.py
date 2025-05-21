from collections import Counter

"""
stack을 활용해서 풀어야한다.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        stack = []
        map = {
            '}': '{',
            ')': '(',
            ']': '['
        }
    
        for s in s_list:
            if s in map.values():
                stack.append(s)
            else:
                if stack and map[s]==stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        return True


"""
다음과 같이 푼 코드를 봤는데 훨씬 깔끔하고 이해하기도 편하다.
""" 
class Solution:
    def isValid(self, s: str) -> bool:
        op = '({['
        valid_pairs = ('()', '{}', '[]')
        stack = []
        for c in s:
            if c in op:
                stack.append(c)
            elif not stack or stack.pop() + c not in valid_pairs:
                return False
        return not stack
        



solution = Solution()
s = "()[]{}"
answer = solution.isValid(s)
print(f"answer >> {answer}")