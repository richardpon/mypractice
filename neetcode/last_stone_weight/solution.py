import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x != y:
                diff = abs(abs(x) - abs(y))
                heapq.heappush(heap, -diff)

        if len(heap) == 1:
            return -heap[0]
        else:
            return 0

