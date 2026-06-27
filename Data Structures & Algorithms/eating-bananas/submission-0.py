from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def solver(speed):
            hrs = 0
            for pile in piles:
                hrs += ceil(pile / speed)
            return hrs

        l = 1
        r = max(piles)
        ans = r

        while l <= r:
            k = (l + r) // 2
            hrs = solver(k)

            if hrs <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1

        return ans