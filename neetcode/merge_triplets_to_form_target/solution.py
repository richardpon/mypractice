class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        has_match = [False for _ in range(3)]
        
        for x,y,z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            if x == target[0]:
                has_match[0] = True
            if y == target[1]:
                has_match[1] = True
            if z == target[2]:
                has_match[2] = True

        return all(has_match)

