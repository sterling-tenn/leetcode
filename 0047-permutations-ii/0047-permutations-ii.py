class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # base case, 1 element -> 1 permutation
        if len(nums) == 1:
            return [nums]
        
        # recursive case
        res = []
        for idx, num in enumerate(nums):
            remaining = nums[:idx] + nums[idx + 1:]
            
            for perm in self.permuteUnique(remaining):
                if [num] + perm not in res: # if unique
                    res.append([num] + perm)
        
        return res