class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            need = target - nums[i]
            if need in nums[i+1:]:
                j = nums[i+1:].index(need)
                return [i, j + i + 1]
        