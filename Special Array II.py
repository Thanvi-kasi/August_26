class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        prefix = [0] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1]

            if nums[i] % 2 == nums[i - 1] % 2:
                prefix[i] += 1

        answer = []

        for left, right in queries:
            bad_pairs = prefix[right] - prefix[left]

            answer.append(bad_pairs == 0)

        return answer
