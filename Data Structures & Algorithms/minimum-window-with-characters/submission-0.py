class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s += " "
        frequency_dict_t = dict()
        frequency_dict_s = dict()
        filled = 0
        l = 0
        r = 0
        result_l = 0
        result_r = 0
        min_diff = len(s)

        for sub_s in t:
            frequency_dict_t[sub_s] = frequency_dict_t.get(sub_s, 0) + 1

        while r != len(s):
            while filled == len(frequency_dict_t):
                min_diff = min(min_diff, r-l+1)

                if min_diff == r - l + 1:
                    result_l = l
                    result_r = r

                if s[l] in frequency_dict_s:
                    frequency_dict_s[s[l]] -= 1

                    if frequency_dict_s[s[l]] < frequency_dict_t[s[l]]:
                        filled -= 1

                    if frequency_dict_s[s[l]] == 0:
                        frequency_dict_s.pop(s[l])

                l += 1

            if s[r] in frequency_dict_t:
                frequency_dict_s[s[r]] = frequency_dict_s.get(s[r], 0) + 1

                if frequency_dict_s[s[r]] == frequency_dict_t[s[r]]:
                    filled += 1

            r += 1

        return s[result_l:result_r] if s[result_l:result_r] != s else ""
