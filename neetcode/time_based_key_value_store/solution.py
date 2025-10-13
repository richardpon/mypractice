class TimeMap:

    def __init__(self):
        self.store: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        sorted_values = self.store[key]

        if not sorted_values:
            return ""


        left = 0
        right = len(sorted_values) - 1
        most_recent:tuple[int,str] = None
        while left <= right:
            i = right - left // 2
            cur_timestamp, cur_val = sorted_values[i]
            
            if cur_timestamp <= timestamp:
                # Consider this as a candidate to return
                if not most_recent or most_recent[0] < cur_timestamp:
                    most_recent = sorted_values[i]
                left = i + 1
            else:
                right = i - 1

        if most_recent:
            return most_recent[1]
        
        return ""
