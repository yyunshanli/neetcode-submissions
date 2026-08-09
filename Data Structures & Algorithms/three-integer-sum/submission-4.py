class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            
            if i > 0 and n == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr = n + nums[r] + nums[l]
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    res.append([n, nums[r], nums[l]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        return res
            

                


        