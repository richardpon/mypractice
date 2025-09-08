class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # val_to_count:dict[int,int]

        val_to_count:dict[int,int] = defaultdict(int)
        for n in nums:
            val_to_count[n] += 1

        values_ordered = [k for k,v in sorted(val_to_count.items(), key=lambda x: x[1])]

        output = []
        
        for i,sorted_value in enumerate(values_ordered[::-1]):
            if i >= k:
                break
            
            output.append(sorted_value)
        
        return output


