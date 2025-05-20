from collections import Counter

"""
permutations로 구현할 경우 memory limit exceeded에러가 발생한다.
슬라이딩 윈도우를 활용해 윈도우 안에 문자열과 s1의 문자열의 string 빈도를 확인한다
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_counter = Counter(s1)

        for i in range(len(s2)):
            s2_counter = Counter(s2[i:k+i])
            if s1_counter == s2_counter:
                return True

        return False
    
solution = Solution()
s1 = "ab"
s2 = "eidboaoo" 
answer = solution.checkInclusion(s1, s2)
print(f"answer >> {answer}")