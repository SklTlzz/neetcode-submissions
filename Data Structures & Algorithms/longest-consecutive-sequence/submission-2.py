class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len_seq = 0
        curr_len_seq = 1
        set_nums = set(nums)

        for num in set_nums:
            curr_num = num + 1

            if num - 1 not in set_nums:
                while curr_num in set_nums:
                    curr_len_seq += 1
                    curr_num += 1

            max_len_seq = max(max_len_seq, curr_len_seq)
            curr_len_seq = 1

        return max_len_seq
