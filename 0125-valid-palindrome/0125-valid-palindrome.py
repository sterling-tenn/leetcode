class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = ''
        for char in s:
            if char.isalnum():
                alphanum += char.lower()
        
        # check if the first half matches the mirror of the second half
        for i in range(len(alphanum) // 2):
            if alphanum[i] != alphanum[len(alphanum) - 1 - i]:
                return False
            
        return True