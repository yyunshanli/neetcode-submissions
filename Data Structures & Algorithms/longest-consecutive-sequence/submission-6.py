class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)== 0): return 0
        nums.sort()
        maxc = 1
        temp = 1
        for i in range(0, len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            if nums[i+1] == nums[i] +1:
                temp += 1
                maxc = max(maxc, temp)
            else:
                temp = 1
        return maxc
        