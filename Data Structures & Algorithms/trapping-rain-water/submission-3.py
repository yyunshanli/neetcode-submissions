class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        r, l = len(height) - 1, 0
        rightMax, leftMax = height[r], height[l]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res




        # res = 0
        # n = len(height)

        # leftMax = [0] * n
        # rightMax = [0] * n

        # leftMax[0] = height[0]
        # for i in range(1, n):
        #     leftMax[i] = max(leftMax[i-1], height[i])

        # rightMax[n-1] = height[n-1]
        # for j in range(n-2, -1, -1):
        #     rightMax[j] = max(rightMax[j+1], height[j])

        # print(leftMax)
        # print(rightMax)

        # for i in range(n):
        #     res += min(rightMax[i], leftMax[i]) - height[i]
        
        # return res


        ## brute force 
        # res = 0

        # for i in range(len(height)):
        #     leftMax, rightMax = height[i], height[i] 

        #     for j in range(i):
        #         leftMax = max(leftMax, height[j])
        #     for k in range(len(height) - 1, i, -1):
        #         rightMax = max(rightMax, height[k])
        #     res += min(leftMax, rightMax) - height[i]
        # return res

        