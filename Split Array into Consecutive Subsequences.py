class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = {}
        need = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        for x in nums:
         
            if freq[x] == 0:
                continue

            freq[x] -= 1

            if need.get(x, 0) > 0:
                need[x] -= 1
                need[x + 1] = need.get(x + 1, 0) + 1

            else:
                if freq.get(x + 1, 0) == 0 or freq.get(x + 2, 0) == 0:
                    return False

                freq[x + 1] -= 1
                freq[x + 2] -= 1

                need[x + 3] = need.get(x + 3, 0) + 1

        return True
