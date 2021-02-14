class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        
        for num in nums1:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
                
        output = []
        for num in nums2:
            if num in counts:
                if counts[num] > 1:
                    counts[num] -= 1
                else:
                    del counts[num]
                output.append(num)
                
        return output
            
            