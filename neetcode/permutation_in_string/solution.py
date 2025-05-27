from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        c1 = Counter(s1)

        l = len(s1)

        c2 = Counter(s2[:l])
        for i in range(len(s2) - l + 1):
            if c1 == c2:
                return True
            
            #increment
            c2.subtract(s2[i])
            
            # not for last iteration
            if i+l < len(s2):
                c2.update(s2[i+l])
        
        return False



