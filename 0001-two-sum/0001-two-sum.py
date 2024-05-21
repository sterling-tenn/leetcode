class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {} # keep track of the numbers we've seen and their indexes
        
        for idx, num in enumerate(nums):
            diff = target - num
            
            # have we seen the required difference value before?
            if diff in hashmap.keys():
                return [idx, hashmap[diff]]
            
            hashmap[num] = idx # add the current number and index