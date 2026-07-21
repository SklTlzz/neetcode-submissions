class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_subs_len = 0
        curr_sub_s = set()

        while r != len(s):
            while s[r] in curr_sub_s:
                curr_sub_s.remove(s[l])
                l += 1

            curr_sub_s.add(s[r])
            max_subs_len = max(max_subs_len, len(curr_sub_s))
            r += 1

        max_subs_len = max(max_subs_len, len(curr_sub_s))

        return max_subs_len
