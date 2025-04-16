"""
Notes: I mistead the question and thought the subawway had to be returned, not the sum

This complicated the solutio, but oh well.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        O(n) traversal
        maintain current best sub array

        - how to know when to reset?
        -- when subarray total < 0? (yes, if current subarray >= 1, beneficial to add it to)


        input [5,4,-1,7,8]
        
        best_so_far [5,4] (9)

        sub-array-so-far [5,4,-1] (to be added to future inputs)
        - reset when sum < 1

        if sub_array_sum_so_far > best_so_far:
            track_it
        """

        best_so_far = []
        best_sum_so_far = None
        
        # reset when sum < 1 (otherwise, keep it)
        # "current" sum that may be part of "best"
        sub_array_so_far = []
        sub_array_sum_so_far = None

        for num in nums:
            # first number (have to have at least one number)
            if best_sum_so_far is None:
                best_so_far.append(num)
                best_sum_so_far = num
                sub_array_so_far.append(num)
                sub_array_sum_so_far = num
                continue

            # add it (maybe) beneficial
            ## positive number always beneficial
            if num > 0:
                # may be best if previous was negative
                if num > best_sum_so_far and best_sum_so_far < 0:
                    best_so_far = [num]
                    best_sum_so_far = num
                    sub_array_so_far = [num]
                    sub_array_sum_so_far = num
                    continue

                sub_array_so_far.append(num)
                sub_array_sum_so_far += num

                # is new best?
                if sub_array_sum_so_far > best_sum_so_far:
                    best_so_far = sub_array_so_far
                    best_sum_so_far = sub_array_sum_so_far

            ## zero or negative maybe beneficial
            else:
                # better negative number
                if num > best_sum_so_far:
                    best_so_far = [num]
                    best_sum_so_far = num
                    sub_array_sum_so_far = num
                    sub_array_so_far = [num]
                    continue

                else:
                    #consider if <=0 is maybe beneficial to keep around for later
                    # edge case of not adding zero???
                    sub_array_so_far.append(num)
                    sub_array_sum_so_far += num

                    # is <=0 maybe beneficial (do nothing or reset)
                    if sub_array_sum_so_far <= 0:
                        # reset as there's no point in keeping this around
                        sub_array_so_far = []
                        sub_array_sum_so_far = 0

        return best_sum_so_far    

        """
        when does sub_array_so_far become the new best?

        what about all negative numbers
        """

