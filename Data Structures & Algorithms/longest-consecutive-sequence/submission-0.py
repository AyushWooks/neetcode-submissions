class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        longest = 0
        for i in nums:
            if (i - 1) not in st:
                length = 0
                while (i + length) in st:
                    length += 1
                    longest = max(length, longest)
        return longest