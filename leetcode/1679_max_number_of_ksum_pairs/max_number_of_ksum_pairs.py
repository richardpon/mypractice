from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #build dict element->number of occurrences

        tracker = Tracker()
        num_pairs = 0

        for num in nums:
            target = k - num

            # case 1: target num already exists in tracker (already been traversed)
            if tracker.has(target):
                # found a match!
                num_pairs += 1
                tracker.remove(target)

            # case 2: save num for future (no match right now)
            else:
                tracker.add(num)

            
        return num_pairs
    
    
class Tracker:

    def __init__(self):
        self.count = {}

    def add(self, num):
        if num in self.count:
            self.count[num] += 1
        else:
            self.count[num] = 1
    
    def remove(self, num):
        if self.count[num] > 1:
            self.count[num] -= 1
        else:
            del self.count[num]

    def has(self,num):
        return num in self.count

    def size(self):
        return len(self.count.keys())

    def get_random_num(self):
        return list(self.count.keys())[0]



