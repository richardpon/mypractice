from typing import List, Dict, Tuple, Set
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # At most 3 copies of 0, or 2 copies of non-zero
        nums_count = {} #Dict[int,int] #Dict[n, count]
        for num in nums:
            if num in nums_count:
                nums_count[num] = nums_count[num] + 1
            else:
                nums_count[num] = 1

        # build nums with max 3 instances of each number
        nums = []
        for num in nums_count.keys():
            num_count = nums_count[num]
            if num == 0:
                num_max = 3
            else:
                num_max = 2
                
            for i in range(0, min(num_count, num_max)):
                nums.append(num)
        
        if len(nums) < 3:
            return []

        # Dict[int, List[int]] # Dict[num: indices]
        num_to_index_dict = {}
        for i in range(0, len(nums)):
            cur_num = nums[i]
            if cur_num in num_to_index_dict:
                cur_indexes = num_to_index_dict[cur_num] # List[int]
                cur_indexes.append(i)
                num_to_index_dict[cur_num] = cur_indexes
            else:
                num_to_index_dict[cur_num] = [i]

        # potential output of ordered sets to dedupe
        output_sets = set()

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a = nums[i]
                b = nums[j]

                if -(a + b) in num_to_index_dict:
                    # possible matches List[int]
                    possible_indexes = num_to_index_dict.get(-a-b)
                    for k in possible_indexes:
                        if k != i and k != j:
                            #yay, we found unique indexes
                            indices = [a, b, -a-b]
                            indices.sort()
                            output_sets.add((indices[0], indices[1], indices[2]))

        # convert sets to lists
        output = []
        for set_of_nums in output_sets:
            list_of_nums = [set_of_nums[0], set_of_nums[1], set_of_nums[2]]
            output.append(list_of_nums)

        output.sort()
        return output



nums = [-1,0,1,2,-1,-4,-1,-1,-1]

s = Solution()               

ret = s.threeSum(nums)
print("___")
print(ret)


