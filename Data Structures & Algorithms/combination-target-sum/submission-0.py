class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def recursion(i, curr, arr):
            if curr > target:
                return
            if curr == target:
                res.append(arr[:])
                return
            for j in range(i, len(nums)):
                arr.append(nums[j])
                recursion(j, curr + nums[j], arr)
                arr.pop()

        recursion(0, 0, [])
        return res




            
        