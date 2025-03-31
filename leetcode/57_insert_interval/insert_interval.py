class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return self.insert_all(intervals, [newInterval])
    
    def insert_all(self, intervals_a: List[List[int]],  intervals_b: List[List[int]]) -> List[List[int]]:
        """
        combines intervals_a and intervals_b, where elements from each can overlap a single
        """

        # either empty?
        if not intervals_a:
            return intervals_b
        if not intervals_b:
            return intervals_a

        first_a = intervals_a[0]
        first_b = intervals_b[0]

        # interval_a is before (non-overlapped)
        if first_a[1] < first_b[0]:
            return [first_a] +self.insert_all(intervals_a[1:], intervals_b)
        if first_b[1] < first_a[0]:
            return [first_b] + self.insert_all(intervals_a, intervals_b[1:])

        # complete overlap (one inside the other)
        # a surrounds b
        if first_a[0] <= first_b[0] and first_a[1] >= first_b[1]:
            return self.insert_all(intervals_a, intervals_b[1:])

        # b surrounds a
        if first_b[0] <= first_a[0] and first_b[1] >= first_a[1]:
            return self.insert_all(intervals_a[1:], intervals_b)

        # partial overlap
        start = min(first_a[0], first_b[0])
        end = max(first_a[1], first_b[1])

        return self.insert_all(intervals_a[1:], [[start,end]])

