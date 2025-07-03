class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            s = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / s)
            if  totalTime <= h:
                r = s - 1
                res = s
            else:
                l = s + 1
        
        return res
