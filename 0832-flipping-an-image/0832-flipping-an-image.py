class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for l in image:
            res.append(self.invert(self.flip(l)))
        return res
        
    def flip(self, l: List[int]) -> List[int]:
        return reversed(l)
        
    def invert(self, l: List[int]) -> List[int]:
        return [1 - i for i in l]