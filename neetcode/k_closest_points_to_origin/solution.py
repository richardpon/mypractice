import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # list[list[list[int]], float]
        points_and_dist = []

        for point in points:
            d = math.sqrt(point[0]**2 + point[1]**2)
            points_and_dist.append([point, d])
            
        sorted_by_d = sorted(points_and_dist, key=lambda p: p[1])    


        kth_pairs = sorted_by_d[:k]
        return [pair[0] for pair in kth_pairs]
        
        
