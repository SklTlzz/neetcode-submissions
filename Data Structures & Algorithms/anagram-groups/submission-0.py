class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        alphabet = {chr(i): i - 97 for i in range(97, 123)}
        hash_map = dict()

        for string in strs:
            counter = [0]*26

            for elem in string:
                counter[alphabet[elem]] += 1

            hash_map[tuple(counter)] = hash_map.get(tuple(counter), []) + [string]

        for value in hash_map.values():
            result.append(value)

        return result
