class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            # opening bracket
            if char in "({[":
                stack.append(char)
            # closing bracket
            else:
                # starts with closing bracket - invalid
                if not stack:
                    return False
                if char == ")" and stack[-1] != "(":
                    return False
                if char == "}" and stack[-1] != "{":
                    return False
                if char == "]" and stack[-1] != "[":
                    return False
                stack.pop()
                
        # openening bracket was never closed
        if len(stack) != 0:
            return False
        
        return True