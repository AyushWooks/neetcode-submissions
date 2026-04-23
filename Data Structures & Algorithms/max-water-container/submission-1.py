class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            min_h = min(heights[left],heights[right])
            length = right - left 
            water = min_h * length
            max_water = max(max_water, water)
            if min_h == heights[left]:
                left += 1
            else:
                right -= 1
        return max_water
