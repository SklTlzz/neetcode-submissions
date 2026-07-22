class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        r = 0
        sorted_s1 = sorted(s1)

        while r != len(s2):
            if r - l + 1 == len(s1):
                if sorted_s1 == sorted(s2[l:r+1]):
                    return True
                
                l += 1

            r += 1

        return False
