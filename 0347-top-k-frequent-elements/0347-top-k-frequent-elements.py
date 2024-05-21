class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # count and keep track of occurrences
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        sorted_by_values = sorted(hashmap, key = lambda x : hashmap[x], reverse = True)
        
        # append k values to the result
        res = []
        for idx, num in enumerate(sorted_by_values):
            if k == idx:
                break
            res.append(num)
            
        return res