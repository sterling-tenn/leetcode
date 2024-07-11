class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        
        for x, y in points:
            d_squared = x**2 + y**2
            minheap.append([d_squared, x, y])
        heapq.heapify(minheap)
        
        res = []
        for _ in range(k):
            d_squared, x, y = heapq.heappop(minheap)
            res.append([x,y])
        return res