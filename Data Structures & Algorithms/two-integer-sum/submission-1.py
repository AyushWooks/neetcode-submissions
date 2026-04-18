class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summ = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in summ:
                return [summ[rem], i]
            summ[nums[i]] = i 
        return False