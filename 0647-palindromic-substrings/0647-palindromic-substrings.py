class Solution:
    def countSubstrings(self, s: str) -> int:
        n = 0
        
        for i in range(len(s)):
            l = r = i
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                n += 1
                l -= 1
                r += 1
                
            l, r = i, i+1
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                n += 1
                l -= 1
                r += 1
        return n