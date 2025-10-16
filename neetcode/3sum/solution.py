class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        #value_to_indexes: dict[int, set[int]]
        sum_to_indexes: dict[int, set[tuple[int,int]]]
        """

        sum_to_indexes: dict[int, set[tuple[int,int]]] = defaultdict(set)

        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:], start=i+1):
                cur_sum = n + m
                sum_to_indexes[cur_sum].add((i,j))

        index_triplets = set()
        for k, num in enumerate(nums):
            if -num in sum_to_indexes:
                for i,j in sum_to_indexes[-num]:
                    if k == i or k == j:
                        continue
                    index_triplet = [i,j,k]
                    index_triplet.sort()
                    index_triplets.add(tuple(index_triplet))

        triplets = set()
        for i,j,k in index_triplets:
            cur_nums=[nums[i], nums[j], nums[k]]
            cur_nums.sort()
            triplets.add(tuple(cur_nums))

        output = []
        for a,b,c in triplets:
            output.append([a,b,c])

        return output

        
