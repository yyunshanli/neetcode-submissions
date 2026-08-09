class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l<r:
            while l<r and not (s[l].isalpha() or s[l].isalnum()):
                l+= 1
            while r>l and not (s[r].isalpha() or s[r].isalnum()):
                r-= 1
            print(s[r],s[l])
            if(s[r].lower() != s[l].lower()):
                return False
            r -=1
            l += 1
        return True
