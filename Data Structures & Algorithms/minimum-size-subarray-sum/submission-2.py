class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_count = float('+inf')
        summ = 0
        l = 0
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                min_count = min(r - l + 1 , min_count)
                summ -= nums[l]
                l += 1
        return 0 if min_count == float('inf') else min_count
            