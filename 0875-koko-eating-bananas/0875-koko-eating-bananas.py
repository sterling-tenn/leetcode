class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_spd, max_spd = 1, max(piles)
        
        while min_spd <= max_spd:
            mid_spd = min_spd + ((max_spd - min_spd) // 2)
            
            t = 0
            for p in piles:
                t += math.ceil(p / mid_spd)
            
            if t > h: # gotta eat faster
                min_spd = mid_spd + 1
            else: # can eat slower
                max_spd = mid_spd - 1
                
        return min_spd