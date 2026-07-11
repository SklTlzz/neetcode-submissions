class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(nums)
        max_len_seq = 1
        curr_len_seq = 1

        for i in range(1, len(sorted_nums)):
            if (sorted_nums[i - 1] + 1 == sorted_nums[i]):
                curr_len_seq += 1
                max_len_seq = max(max_len_seq, curr_len_seq)
            elif (sorted_nums[i - 1] == sorted_nums[i]):
                continue
            else:
                max_len_seq = max(max_len_seq, curr_len_seq)
                curr_len_seq = 1

        return max_len_seq
