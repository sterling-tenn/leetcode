class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        in_window = set()
        l, r = 0, 0
        
        longest = 0
        while r < len(s):
            while s[r] in in_window:
                in_window.remove(s[l])
                l += 1
                
            in_window.add(s[r])
            length = r - l + 1
            longest = max(longest, length)
            
            r += 1
        return longest
        