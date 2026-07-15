class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for string in strs:
            encoded_str += str(len(string)) + "#" + string

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        curr_idx = 0

        while curr_idx < len(s):
            prev_idx = s.find("#", curr_idx)
            curr_len = int(s[curr_idx:prev_idx])

            curr_str = s[prev_idx + 1:prev_idx + 1 + curr_len]
            decoded_strs.append(curr_str)
            
            curr_idx = prev_idx + 1 + curr_len

        return decoded_strs
