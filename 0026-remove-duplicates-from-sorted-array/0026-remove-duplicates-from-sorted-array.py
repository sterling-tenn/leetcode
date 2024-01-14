class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
    
        uniques = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[uniques] = nums[i]
                prev = nums[uniques]
                uniques += 1
                
        return uniques
        