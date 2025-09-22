class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        output = []
        for i in range(len(intervals)):
            
            cur_interval = intervals[i]

            # new comes before (no overlap_)
            if newInterval[1] < cur_interval[0]:
                output.append(newInterval)
                output.extend(intervals[i:])
                return output

            # new is after (no overlap)
            elif cur_interval[1] < newInterval[0]:
                output.append(cur_interval)

            # combine
            else:
                combined_interval = [
                    min(cur_interval[0], newInterval[0]),
                    max(cur_interval[1], newInterval[1]),
                ]
                newInterval = combined_interval
    
        output.append(newInterval)

        return output

