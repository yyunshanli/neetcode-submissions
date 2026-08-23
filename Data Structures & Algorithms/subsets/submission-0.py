class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recursion(i, curr):
            if i == len(nums):
                res.append(curr)
                return

            recursion(i+1, curr +[nums[i]])
            recursion(i+1, curr)
        recursion(0, [])
        return res
        



        
        