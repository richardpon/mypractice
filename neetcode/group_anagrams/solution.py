class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_to_strs: dict[str, list[str]] = {}
        
        for cur_str in strs:
            key = "".join(sorted(cur_str))

            if key not in hash_to_strs:
                hash_to_strs[key] = []
            hash_to_strs[key].append(cur_str)

        return hash_to_strs.values()


