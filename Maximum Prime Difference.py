class Solution:
    def maximumPrimeDifference(self, nums):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        first = -1
        last = -1

        for i, num in enumerate(nums):
            if is_prime(num):
                if first == -1:
                    first = i
                last = i

        return last - first
