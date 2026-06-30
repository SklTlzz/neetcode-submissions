class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string = encoded_string + str(len(string)) + "#" + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        curr_len = 0
        i = 0
        prev_i = 0

        while i != len(s):
            if s[i] == "#":
                curr_len = int(s[prev_i:i])
                curr_string = s[i + 1:i + 1 + curr_len]
                decoded_string.append(curr_string)

                i += curr_len + 1
                prev_i = i
            else:
                i += 1
            
        return decoded_string
