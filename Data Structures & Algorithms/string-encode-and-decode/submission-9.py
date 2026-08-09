class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        print(s)

        i = 0
        while i < len(s):
            read_in = s[i]
            while i + 1 < len(s) and s[i + 1] != '#':
                i += 1
                read_in += s[i]
            # print(read_in)
            read_in = int(read_in)
            res.append(s[i+2:i+2+read_in])
            i += read_in + 2
        return res
