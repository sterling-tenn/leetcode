class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        
        while len(maxheap) > 1:
            bigger, smaller = heapq.heappop(maxheap), heapq.heappop(maxheap)
            if bigger < smaller:
                heapq.heappush(maxheap, bigger - smaller)
        
        return (-maxheap[0]) if maxheap else 0