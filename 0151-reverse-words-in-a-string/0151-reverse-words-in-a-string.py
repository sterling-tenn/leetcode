class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = list(filter(lambda x : x != "", s)) # filter out all empty strings
        
        # iterate half from the beginning and swap with the end
        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
            
        return " ".join(s)