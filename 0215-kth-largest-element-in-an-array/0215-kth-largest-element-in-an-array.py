class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-num for num in nums]
        heapq.heapify(maxheap)
        
        for _ in range(k):
            res = -heapq.heappop(maxheap)
        return res