class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def solver(w):
            day = 1
            summ = 0

            for i in range(len(weights)):
                if summ + weights[i] > w:
                    day += 1
                    summ = weights[i]
                else:
                    summ += weights[i]

            return day

        l = max(weights)
        r = sum(weights)
        ans = r

        while l <= r:
            weight = (l + r) // 2
            day = solver(weight)

            if day > days:
                l = weight + 1
            else:
                ans = weight
                r = weight - 1

        return ans