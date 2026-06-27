class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def solver(capacity):
            day = 1
            curr = 0

            for weight in weights:
                if curr + weight > capacity:
                    day += 1
                    curr = weight
                else:
                    curr += weight

            return day

        l = max(weights)
        r = sum(weights)
        ans = r

        while l <= r:
            mid = (l + r) // 2
            required_days = solver(mid)

            if required_days > days:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1

        return ans