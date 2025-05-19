class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = ''

        # 정렬하기
        strs.sort(key=lambda x:len(x))

        for idx, value in enumerate(strs[0]):
            for j in strs[1:]:
                if j[idx] != value:
                    return strs[0][:idx]
        return strs[0]
    
solution = Solution()
strs = ["flower","flow","flight"]
answer = solution.longestCommonPrefix(strs)
print(f"answer >> {answer}")