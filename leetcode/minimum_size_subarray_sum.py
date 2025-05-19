class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        n = len(nums)
        left = 0
        curr = 0
        best = float('inf')

        for right in range(n):
            curr += nums[right]  # 오른쪽 확장
            
            while curr >= target:
                best = min(best, right - left + 1)
                curr -= nums[left]
                left += 1
        
        if best == float('inf'):
            return 0
        else:
            return best
    
solution = Solution()
target = 7
nums = [2,3,1,2,4,3]
answer = solution.minSubArrayLen(target, nums)
print(f"answer >> {answer}")