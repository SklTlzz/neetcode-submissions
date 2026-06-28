class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            hash_map_s = dict()
            hash_map_t = dict()

            for i in s:
                if i in hash_map_s:
                    hash_map_s[i] += 1
                else:
                    hash_map_s[i] = 1

            for i in t:
                if i in hash_map_t:
                    hash_map_t[i] += 1
                else:
                    hash_map_t[i] = 1

            return hash_map_s == hash_map_t
