class Solution:
    def lengthOfLongeastSubstring(self, s: str) -> int:
        answer = 0

        indexs: list = []
        for i in s:
            indexs.append(s.index(i))

        temp = []
        # 등차수열까지만 가져오기
        for i in range(0, len(indexs)-1):
            if indexs[i+1] - indexs[i] == 1:
                temp.append(i)
            else:
                
        print(f"temp >> {temp}")

        return answer

solution = Solution()
s = "abcabcbbb"
solution.lengthOfLongeastSubstring(s)