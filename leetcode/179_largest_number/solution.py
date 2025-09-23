from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare_numbers(a: str, b: str):

            for i in range(max(len(a),len(b)) * 2):
                val_a = a[i % len(a)]
                val_b = b[i % len(b)]

                if val_a < val_b:
                    return -1
                elif val_a > val_b:
                    return 1
            return 0

            
        strs = [str(n) for n in nums]
        strs.sort(key=cmp_to_key(compare_numbers))

        # keep one zero if only zeros
        if all(x == '0' for x in strs):
            strs = ["0"]
        
        output = ""
        for s in strs[::-1]:
            output += s

        return output


