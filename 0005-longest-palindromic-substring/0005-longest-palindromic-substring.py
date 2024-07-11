class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0
        
        for i in range(len(s)):
            l = r = i
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                length = r - l + 1
                if length > max_len:
                    res = s[l:r+1]
                    max_len = length
                l -= 1
                r += 1
                    
            l, r = i, i + 1
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                length = r - l + 1
                if length > max_len:
                    res = s[l:r+1]
                    max_len = length
                l -= 1
                r += 1
        return res