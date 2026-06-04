from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        freq = defaultdict(int)
        freq[0] = 1

        currSum = 0
        count = 0

        for num in nums:
            currSum += num

            count += freq[currSum - k]

            freq[currSum] += 1

        return count