class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l
            maxHeight = min(heights[l], heights[r])
            area = width * maxHeight
            max_a = max(max_a, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1

        return max_a
