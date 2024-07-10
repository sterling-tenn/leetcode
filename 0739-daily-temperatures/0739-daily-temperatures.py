class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [temperature, index]
        for idx, tmp, in enumerate(temperatures):
            while stack and stack[-1][0] < tmp:
                t, i = stack.pop()
                res[i] = idx - i
            stack.append([tmp, idx])
        return res