from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        k = len(s1)
        l = 0
        mp = {}

        count = Counter(s1)

        for r in range(len(s2)):
            mp[s2[r]] = 1 + mp.get(s2[r], 0)
            if r - l + 1 > k:
                mp[s2[l]] -= 1
                if mp[s2[l]] == 0:
                    del mp[s2[l]]
                l += 1
            if r - l + 1 == k:
                if mp == count:
                    return True

        return False