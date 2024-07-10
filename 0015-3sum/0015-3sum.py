class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, num_a in enumerate(nums):
            if idx != 0 and num_a == nums[idx - 1]:
                continue
            
            # twosum
            l, r = idx + 1, len(nums) - 1
            while l < r:
                sum = num_a + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([num_a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
        return res