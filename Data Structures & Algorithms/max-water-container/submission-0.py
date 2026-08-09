class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights) - 1

        while  l < r:
            right, left = heights[r], heights[l]
            curr = min(right, left) * (r - l)
            res = max(res, curr)

            if right > left:
                l += 1
            else:
                r -= 1
        return res
        