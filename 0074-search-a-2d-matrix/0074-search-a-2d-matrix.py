class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for nums in matrix:
            if self.binarySearch(nums, target):
                return True
        return False
    
    # Binary Search https://leetcode.com/problems/binary-search/
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return True
                
        return False