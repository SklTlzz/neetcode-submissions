class Solution:
    def minWindow(self, s: str, t: str) -> str:
        frequency_dict_t = dict()
        frequency_dict_s = dict()
        filled = 0
        l = 0
        r = 0
        result_l = 0
        result_r = 0
        min_diff = float("inf")

        for sub_s in t:
            frequency_dict_t[sub_s] = frequency_dict_t.get(sub_s, 0) + 1

        while r != len(s):
            if s[r] in frequency_dict_t:
                frequency_dict_s[s[r]] = frequency_dict_s.get(s[r], 0) + 1

                if frequency_dict_s[s[r]] == frequency_dict_t[s[r]]:
                    filled += 1

            while filled == len(frequency_dict_t):
                if min_diff > (r - l + 1):
                    min_diff = r - l + 1
                    result_l = l
                    result_r = r + 1

                if s[l] in frequency_dict_s:
                    frequency_dict_s[s[l]] -= 1

                    if frequency_dict_s[s[l]] < frequency_dict_t[s[l]]:
                        filled -= 1

                    if frequency_dict_s[s[l]] == 0:
                        frequency_dict_s.pop(s[l])

                l += 1

            r += 1

        return "" if min_diff == float("inf") else s[result_l:result_r]
