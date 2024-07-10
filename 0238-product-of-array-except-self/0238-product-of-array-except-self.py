class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        prefix[0] = nums[0]
        postfix[-1] = nums[-1]
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
            postfix[len(nums) - 1 - i] = postfix[len(nums) - i] * nums[len(nums) - 1 - i]
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[i + 1])
            elif i == (len(nums) - 1):
                res.append(prefix[i - 1])
            else:
                res.append(prefix[i - 1] * postfix[i + 1])
        return res