class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], idx]
            hashmap[num] = idx