import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            d = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, (d, point))

        smallest = heapq.nsmallest(k, heap)
        return [p[1] for p in smallest]

