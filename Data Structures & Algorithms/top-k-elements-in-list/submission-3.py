class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent_elems = []
        elems_by_frequent = [[] for i in range(len(nums) + 1)]
        count_elems_dict = dict()

        for num in nums:
            count_elems_dict[num] = count_elems_dict.get(num, 0) + 1

        for key, value in count_elems_dict.items():
            elems_by_frequent[value].append(key)

        for i in range(len(elems_by_frequent) - 1, -1, -1):
            if elems_by_frequent[i]:
                most_frequent_elems += elems_by_frequent[i]

                if len(most_frequent_elems) >= k:
                    return most_frequent_elems[:k]
