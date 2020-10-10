from typing import List, Dict, Tuple, Set
class Solution:

    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
    Find all unique triplets in the array which gives the sum of zero.

    Notice that the solution set must not contain duplicate triplets.

    Example input [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    input [-1,0,1,2,-1,-4,-1,-1,-1,-1,-1] #same output

    Observations/Thoughts
    1) No duplicates means that any number that exists > 3 times can be removed
      [0,0,0] 
    2) Only 0 can exist 3 times, all other numbers just twice
    3 + 3 + 3 != 0 
    3 + 3 - 6 = 0 # 3 can exist twice

    3) For A+B+C = 0, iterate through every combination
    A+B = -C # no point in searching all values for -C 

    Iterate through combinations of A+B and perform a lookup for C = -(A+B)

    """

    def reduce_nums(self, nums: List[int]) -> List[int]:
        # At most 3 copies of any number
        # count each instance of every number
        nums_count = {} #Dict[number:int, count:int] 
        for num in nums:
            if num in nums_count:
                nums_count[num] = nums_count[num] + 1
            else:
                nums_count[num] = 1

        # build nums with max 3 instances of each number
        reduced_nums = []
        for num in nums_count.keys():
            num_count = nums_count[num]
            for i in range(0, min(num_count, 3)):
                reduced_nums.append(num)
        
        return reduced_nums


    # Dict[num:int, indices:List[int]]
    # input [-1,0,1,2,-1,-4]
    # {-1:[0,4], 0:[1], 1:[2], 2:[3], -4:[5]}                # need index to dedupe A+B+C=0 (don't want C==A, has to be a different number)
    def create_indexes(self, nums: List[int]) -> Dict[int, List[int]]:
        num_to_index_dict = {}
        for i in range(0, len(nums)):
            cur_num = nums[i]
            if cur_num in num_to_index_dict:
                cur_indexes = num_to_index_dict[cur_num] # List[int]
                cur_indexes.append(i)
                num_to_index_dict[cur_num] = cur_indexes
            else:
                num_to_index_dict[cur_num] = [i]
        
        return num_to_index_dict

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # At most 3 copies of any number
        nums = self.reduce_nums(nums)
        
        if len(nums) < 3:
            return []

        # Dict[int, List[int]] # Dict[num: indices]
        num_to_index_dict = self.create_indexes(nums)

        # potential output of sets of Tuples
        # Set[Tuple[int,int,int]]
        get_of_outputs = set()

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
                            get_of_outputs.add((indices[0], indices[1], indices[2]))

        # convert Tuples to lists
        output = []
        for set_of_nums in get_of_outputs:
            list_of_nums = [set_of_nums[0], set_of_nums[1], set_of_nums[2]]
            output.append(list_of_nums)

        output.sort()
        return output



nums = [-1,0,1,2,-1,-4,-1,-1,-1]

s = Solution()               

ret = s.threeSum(nums)
print("___")
print(ret)


