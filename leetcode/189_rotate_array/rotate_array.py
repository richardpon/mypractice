from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        for i in range(0,k):
            nums.insert(0, nums[-1])
            del nums[-1]
            

     