class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = [interval.start for interval in intervals]
        end_times = [interval.end for interval in intervals]
        
        sorted_start = sorted(start_times)
        sorted_end = sorted(end_times)

        max_rooms = 0
        cur_rooms = 0
        
        while sorted_start and sorted_end:
            if sorted_start[0] < sorted_end[0]:
                cur_rooms += 1
                max_rooms = max(max_rooms, cur_rooms)
                sorted_start = sorted_start[1:]

            else:
                cur_rooms -= 1
                sorted_end = sorted_end[1:]
        
        return max_rooms
        

