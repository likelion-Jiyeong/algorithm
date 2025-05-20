class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            curr_sum += nums[i]
            if i >= k - 1 :
                max_sum = max(max_sum, curr_sum)
                curr_sum -= nums[i - k + 1]
            
        max_average = max_sum / k

        return max_average
    
solution = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
answer = solution.findMaxAverage(nums, k)
print(f"answer >> {answer}")