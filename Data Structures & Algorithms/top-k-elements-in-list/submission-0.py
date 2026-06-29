class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent_elems = []
        counter = dict()
        buckets = [[] for i in range(len(nums) + 1)]

        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        for key in counter:
            buckets[counter[key]].append(key)

        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                most_frequent_elems += buckets[i]
                
                if len(most_frequent_elems) >= k:
                    return most_frequent_elems[:k]
