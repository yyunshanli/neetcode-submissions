class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = nums.copy()
        for num in nums:
            new_nums.remove(num)
            if num in new_nums:
                return True

        return False
        