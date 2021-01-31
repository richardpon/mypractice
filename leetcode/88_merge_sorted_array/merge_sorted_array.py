from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        if not nums2:
            return
        elif not nums1:
            nums1 = nums2 #needed?
            return

        i = 0
        while m >= 0 and n > 0:

            if (m == 0 and n > 0) or nums1[i] > nums2[0]:
                #perform insert into nums1
                del nums1[-1]
                nums1.insert(i, nums2[0])

                #remove it from nums2
                nums2 = nums2[1:]
                
                i += 1  
                n -= 1

            else:
                # can't append
                i += 1
                m -=1
