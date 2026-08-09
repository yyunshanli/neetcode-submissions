class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1
        while r > l:
            curr = numbers[r] + numbers[l]
            if(curr == target):
                return (l+1,r+1)
            elif(curr > target):
                r -= 1
            else:
                l+=1

        