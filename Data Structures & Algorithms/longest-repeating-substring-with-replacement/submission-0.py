class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_elems = dict()
        l = 0
        r = 0
        max_subs_len = 0

        while r != len(s):
            count_elems[s[r]] = count_elems.get(s[r], 0) + 1

            while (r - l + 1) - max(count_elems.values()) > k:
                count_elems[s[l]] -= 1
                l += 1

            curr_subs_len = (r - l + 1)
            max_subs_len = max(max_subs_len, curr_subs_len)

            r += 1

        return max_subs_len
