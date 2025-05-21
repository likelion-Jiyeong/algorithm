class Solution:
    """
    1. key: value방식으로 일단 dictionary만든다.
    2. 들어오는 str을 key에서 찾아서 더한다.
    3. 예외 case는 4, 5 처리한다.
        3.1. I가 V, X 전에 위치하면: -1 / X
    """
    def romanToInt(self, s: str) -> int:
        answer = 0
        symbol_map: dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == 'I' and s[i+1] in ['V', 'X']:
                answer += symbol_map[s[i+1]] - 1
                i += 2
            elif i + 1 < len(s) and s[i] == 'X' and s[i+1] in ['L', 'C']:
                answer += symbol_map[s[i+1]] - 10
                i += 2
            elif i + 1 < len(s) and s[i ]== 'C' and s[i+1] in ['D', 'M']:
                answer += symbol_map[s[i+1]] - 100
                i += 2
            else:
                answer += symbol_map[s[i]]
                i += 1

        return answer

solution = Solution()
s = "LVIII"
answer = solution.romanToInt(s)
print(f"answer >> {answer}")