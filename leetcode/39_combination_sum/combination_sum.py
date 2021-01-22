from typing import List
"""
candidates = [2,3,6,7], target = 7
try
[][2,3,6,7], target = 7

[][3,6,7] - remove first
  [][6,7]
    [][7]
    [6][6,7]
  [3][6,7] 
    [3][7]
    [3,6][7] 
[2][2,3,6,7] - add first
  [2][3,6,7] - add first
  [2,3][3,6,7]

[combo] [candidates]

base cases:
 sum(combo) == target -> increment (store ordered tuple of combo in set)
 sum(combo) > target -> stop
 sum(combo) < target -> recurse if len(candidates) > 0

recurse
case 1: don't add 1st element, just remove from candidates
case 2: add 1st element to combo

"""

class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output_set = self.comboSumRecursive(candidates, target, [], 0)
        output = []
        for cur_tuple in output_set:
            output.append(list(cur_tuple))

        return output
        

    def comboSumRecursive(self, 
        candidates: List[int], 
        target: int, 
        combo_so_far: List[int], 
        sum_so_far: int):
        
        if sum_so_far > target:
            return set()
        elif sum_so_far == target:
            combo_so_far.sort()
            return {tuple(combo_so_far)}
        else:
            #recurse
            if candidates:
                # case 1: don't add first element
                set1 = self.comboSumRecursive(candidates[1:], target, combo_so_far.copy(), sum_so_far)
                # case 2: add first element to combo
                cur = candidates[0]
                sum_so_far += cur
                combo_so_far.append(cur)
                set2 = self.comboSumRecursive(candidates, target, combo_so_far, sum_so_far)

                return set1 | set2
            else:
                return set()
        