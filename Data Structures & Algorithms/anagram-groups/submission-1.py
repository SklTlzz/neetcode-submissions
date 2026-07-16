class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        alphabet = {chr(i): i - 97 for i in range(97, 123)}
        dict_of_anagrams = dict()

        for string in strs:
            string_elems_freq = [0]*26

            for sub_s in string:
                string_elems_freq[alphabet[sub_s]] += 1

            dict_of_anagrams[tuple(string_elems_freq)] = dict_of_anagrams.get(tuple(string_elems_freq), []) + [string]

        for value in dict_of_anagrams.values():
            result.append(value)

        return result
