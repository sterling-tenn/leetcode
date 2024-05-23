class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # maximum is the shortest
        shortest = min(strs, key = len)
        strs.remove(shortest)
        
        prefix = ''
        for idx, char in enumerate(shortest):
            for s in strs:
                if s[idx] != char:
                    return prefix
            prefix += char
            
        return prefix