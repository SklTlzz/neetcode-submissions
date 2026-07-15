class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for string in strs:
            encoded_str += str(len(string)) + "#" + string

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        last_str_idx = 0
        curr_idx = 0

        while curr_idx < len(s):
            if s[curr_idx] == "#":
                curr_len = int(s[last_str_idx:curr_idx])
            else:
                curr_idx += 1
                continue

            curr_string = s[curr_idx+1:curr_idx+1+curr_len]
            decoded_strs.append(curr_string)

            last_str_idx = curr_idx + curr_len + 1
            curr_idx += curr_len + 1

        return decoded_strs
