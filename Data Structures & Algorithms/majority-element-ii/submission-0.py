class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = {}
        res = []
        for i in nums:
            mp[i] = 1 + mp.get(i, 0)
        
        for key, val in mp.items():
            if val > len(nums) // 3:
                res.append(key)
        return res