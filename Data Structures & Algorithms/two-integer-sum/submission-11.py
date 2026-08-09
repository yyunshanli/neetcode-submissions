class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            need = target - num
            if need in nums:
                need_idx = nums.index(need)
                if i == need_idx:
                    continue
                return sorted([i, need_idx])

        