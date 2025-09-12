import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        cooldown = [None] * n

        counts = Counter(tasks)

        heap = [(-count, item) for item, count in counts.items()]
        heapq.heapify(heap)
    

        num_tasks_to_process = len(tasks)
        number_cycles = 0
        while num_tasks_to_process > 0:
            # process task (if available)
            if heap:
                task_to_process = heapq.heappop(heap)

                num_tasks_to_process-=1
            
                task_priority, task_id = task_to_process
                task_num_instances = -task_priority - 1

                if task_num_instances > 0:
                    cooldown.append((-task_num_instances, task_id))

            if cooldown[0]:
                heapq.heappush(heap, cooldown[0])
            
            cooldown = cooldown[1:]

            if len(cooldown) < n:
                cooldown.append(None)

            number_cycles+=1

        return number_cycles


