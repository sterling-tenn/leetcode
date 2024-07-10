class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        for num, c in count.items():
            buckets[c].append(num)
            
        res = []
        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res