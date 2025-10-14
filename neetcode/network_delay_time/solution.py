class Solution:
    def __init__(self):
        #src -> [(dest, time)]
        self.times:dict[int, list[tuple[int,int]]] = defaultdict(list)
        
        # node -> time
        self.visited: dict[int, int] = {}

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        for src, dest, time in times:
            self.times[src].append((dest,time))

        self.visit_node(k, 0)

        # visited all nodes
        if len(self.visited) == n:
            return max(self.visited.values())
        
        return -1

    def visit_node(self, node:int, total_time:int):
        # is time better
        if node in self.visited and total_time > self.visited[node]:
            # node was visited before with a better time
            return

        # found node the first time, or found a better time
        self.visited[node] = total_time

        # traverse to childen
        for dest, time in self.times[node]:
            self.visit_node(dest, total_time + time)




