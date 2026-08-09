class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        pre = [1] * n
        suf = [1] * n

        curr = 1
        for i in range(1, n):
            curr *= nums[i-1]
            pre[i] = curr 

        curr = 1

        for i in range(n-2, -1, -1):
            curr *= nums[i + 1]
            suf[i] = curr

        print(suf)


        print(pre)
        res = [1] * n

        for i in range(n):
            res[i] = suf[i] * pre[i]

        return res

        
        