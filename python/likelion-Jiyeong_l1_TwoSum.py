from itertools import combinations
import itertools
from typing import List

    
# Memory Limit Exceeded 에러남 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_ = list(combinations(nums,2))
        ans = []
        result = []
        for value in list_:
            if value[0]+value[1] == target:
                ans = value
                break
        
        result.append(list(filter(lambda x: nums[x]==ans[0], range(len(nums)))))
        result.append(list(filter(lambda x: nums[x]==ans[1], range(len(nums)))))
        
        if len(result[0])>1:
            answer = result[0]
            return answer
        else:
            answer = list(itertools.chain.from_iterable(result))
            return answer

    
obj = Solution()
obj.twoSum([3,3],6)