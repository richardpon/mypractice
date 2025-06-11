from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # build sorted list
        window = SortedList(nums[:k])
        
        # slide window
        output = [window[-1]]
        for i in range(len(nums) - k):
            
            to_remove = nums[i]
            window.remove(to_remove)

            to_add = nums[i+k]
            window.add(to_add)

            output.append(window[-1])

        return output
            

