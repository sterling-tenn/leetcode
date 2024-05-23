class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # track number of letter occurrences in each string
        hash_s = {}
        for char in s:
            hash_s[char] = hash_s.get(char, 0) + 1
        
        hash_t = {}
        for char in t:
            hash_t[char] = hash_t.get(char, 0) + 1
            
        return hash_s == hash_t