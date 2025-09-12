class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subset_list = [[]]

        for num in nums:
            new_subsets = [s+[num] for s in subset_list]
            subset_list.extend(new_subsets)

        return subset_list

