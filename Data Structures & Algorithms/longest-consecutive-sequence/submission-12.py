class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        longest = 0
        length = 1


        for i in n: 
            while(i-length) in n:
                length += 1
                longest = max(longest, length)
            length = 1
            longest = max(longest, length)
        return longest


        # if(len(nums)== 0): return 0
        # nums.sort()
        # maxc = 1
        # temp = 1
        # for i in range(0, len(nums)-1):
        #     if nums[i+1] == nums[i]:
        #         continue
        #     if nums[i+1] == nums[i] +1:
        #         temp += 1
        #         maxc = max(maxc, temp)
        #     else:
        #         temp = 1
        # return maxc
        