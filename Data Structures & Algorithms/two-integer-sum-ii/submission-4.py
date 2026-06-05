class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r= len(nums) - 1

        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                return [l+1, r+1]