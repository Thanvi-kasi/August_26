class Solution:
    def minMaxGame(self, nums):
        while len(nums) > 1:
            n = len(nums)
            newNums = [0] * (n // 2)

            for i in range(n // 2):
                if i % 2 == 0:
                    newNums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    newNums[i] = max(nums[2 * i], nums[2 * i + 1])

            nums = newNums

        return nums[0]
