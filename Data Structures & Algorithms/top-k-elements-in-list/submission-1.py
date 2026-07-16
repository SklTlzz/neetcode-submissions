class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent_elems = []
        elems_by_frequent = {
            i: [] for i in range(len(nums), 0, -1)
        }
        count_elems_dict = dict()

        for num in nums:
            count_elems_dict[num] = count_elems_dict.get(num, 0) + 1

        for key, value in count_elems_dict.items():
            elems_by_frequent[value].append(key)

        for key, value in elems_by_frequent.items():
            if value and len(most_frequent_elems) != k:
                most_frequent_elems += value

        return most_frequent_elems
