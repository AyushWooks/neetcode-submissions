class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            to_find = target - nums[i]
            if to_find in mp:
                return [mp[to_find],i]
            
            mp[nums[i]] = i
        