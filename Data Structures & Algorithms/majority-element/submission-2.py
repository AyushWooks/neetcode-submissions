class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        i = 1
        count = 1
        for i in range(len(nums)):
            if nums[i] != maj:
                count -= 1
            else:
                count += 1
            if count == 0:
                maj = nums[i]
                count = 1
            
        return maj