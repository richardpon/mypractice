from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_length = 0

        i = 0
        while (True):

            if i >= len(nums):
                break
            else:
                current_num = nums[i]

                if current_num == val:
                    # remove it
                    del nums[i]
                else:
                    # keep it
                    new_length += 1
                    i += 1

        return new_length