class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        mp = {}
        mp2 ={}
        l = 0

        for c in s1:
            mp[c] = 1 + mp.get(c,0)
        

        for r in range(len(s2)):
            mp2[s2[r]] = 1 + mp2.get(s2[r],0)

            if r-l+1 > k:
                mp2[s2[l]] -= 1
                if mp2[s2[l]] == 0:
                    del mp2[s2[l]]
                l += 1
            
            if mp == mp2:
                return True
        return False