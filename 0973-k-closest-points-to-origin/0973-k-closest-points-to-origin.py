class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        # calculate distances
        minHeap = []
        for x, y in points:
            dist_squared = (x ** 2) + (y ** 2) # from origin
            minHeap.append([dist_squared, x, y])
            
        # Use minHeap (heapq.heapipfy) for O(n) time complexity, better than brute force and sort which is O(nlogn)
        heapq.heapify(minHeap)
        
        # pop k items from the heap
        res = []
        while k > 0:
            dist_squared, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res