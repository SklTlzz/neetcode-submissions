class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                a = nums[i]
                b = nums[l]
                c = nums[r]

                if a + b + c == 0:
                    triplets.append([a, b, c])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif a + b + c > 0:
                    r -= 1
                else:
                    l += 1

        return triplets
