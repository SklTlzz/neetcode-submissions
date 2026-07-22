class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        r = 0
        s1_elems_count = dict()
        s2_elems_count = {
            s2[l]: 1,
        }

        for sub_s in s1:
            s1_elems_count[sub_s] = s1_elems_count.get(sub_s, 0) + 1

        while r != len(s2):
            if r - l + 1 == len(s1):
                if s2_elems_count == s1_elems_count:
                    return True
                
                s2_elems_count[s2[l]] -= 1
                
                if s2_elems_count[s2[l]] == 0:
                    s2_elems_count.pop(s2[l])
                
                l += 1

            r += 1

            if r != len(s2):
                s2_elems_count[s2[r]] = s2_elems_count.get(s2[r], 0) + 1

        return False
