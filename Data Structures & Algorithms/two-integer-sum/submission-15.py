class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     need = target - nums[i]
        #     if need in nums[i+1:]:
        #         j = nums[i+1:].index(need)
        #         return [i, j + i + 1]

        m = {}

        for i, n in enumerate(nums):
            need = target - n
            if need in m.keys():
                return [m.get(need), i]
            else:
                m[n] = i


        