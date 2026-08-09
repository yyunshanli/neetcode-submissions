class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        l = 0

        while r > l:
            while r > l and (not s[r].isalpha() and not s[r].isalnum()):
                r -= 1
            while r > l and (not s[l].isalpha() and not s[l].isalnum()):
                l += 1
            print(s[r], s[l])
            if s[r].lower() != s[l].lower():
                return False
            r -= 1
            l += 1
        return True
        
        