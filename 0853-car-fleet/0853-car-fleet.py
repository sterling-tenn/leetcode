class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, spd) for pos,spd in zip(position,speed)]
        pairs.sort(reverse=True)
        stack = []
        
        for pos, spd in pairs:
            t = (target - pos) / spd
            stack.append(t)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
                