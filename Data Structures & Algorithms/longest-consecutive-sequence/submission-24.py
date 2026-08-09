class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        length = 1
        res = 0

        for n in nums:
            while n - length in nums:
                length += 1
            res = max(res, length)
            length = 1
            
        return res
        # n = len(nums)

        # res = 0
        # temp = 1

        # for i in range(n-1):
        #     if nums[i] == nums[i+1]:
        #         continue
        #     if nums[i] + 1 == nums[i+1]:
        #         temp += 1
        #         res = max(res, temp)
        #     else:
        #         temp = 1
        # return res


        