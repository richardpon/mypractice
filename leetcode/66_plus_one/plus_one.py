class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        
        carry = 0
        for i in range(0, len(digits)):
            
            # only add to 1st or carry over from prev
            if i == 0 or carry == 1:
                if digits[i] == 9:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] += 1
                    carry = 0
            
        #add extra digit if needed
        if carry == 1:
            digits.append(1)
            
        #reverse
        digits.reverse()
        return digits