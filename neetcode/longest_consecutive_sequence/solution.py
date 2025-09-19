class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)

        starters = []
        for num in num_set:
            if num - 1 not in num_set:
                starters.append(num)

        longest = 0
        for starter in starters:
            for i in range(0,len(nums) + 1):
                if starter + i in num_set:
                    continue
                else:
                    longest = max(longest, i)
                    break
                    
        
        return longest


