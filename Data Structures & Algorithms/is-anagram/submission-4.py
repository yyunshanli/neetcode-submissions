class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}

        for letter_s in s:
            s_map[letter_s] = s_map.get(letter_s, 0) + 1

        for letter_t in t:
            if s_map.get(letter_t, 0) <= 0:
                return False
            else:
                s_map[letter_t] -= 1

        for letter in s_map:
            if s_map[letter] > 0:
                return False
        return True
        