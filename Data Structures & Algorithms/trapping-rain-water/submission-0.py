class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force 
        res = 0

        for i in range(len(height)):
            leftMax, rightMax = height[i], height[i] 

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for k in range(len(height) - 1, i, -1):
                rightMax = max(rightMax, height[k])
            res += min(leftMax, rightMax) - height[i]
        return res

        