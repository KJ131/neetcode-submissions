class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxvol = 0
        while left<right:
            height = min(heights[left], heights[right])
            vol = height * (right - left)
            if maxvol<vol:
                maxvol = vol
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1
                right -= 1
        return maxvol