class Solution:
    def lengthOfLongeastSubstring(self, s: str) -> int:
        max_len, start = 0, 0

        result_dict: dict = {}
        for i in range(len(s)):
            if s[i] in result_dict:
                start = max(start, result_dict[s[i]] + 1)
            result_dict[s[i]] = i
            max_len = max(max_len, i - start + 1)


        return max_len

solution = Solution()
s = "abcabcbbb"
answer = solution.lengthOfLongeastSubstring(s)
print(f"answer >> {answer}")