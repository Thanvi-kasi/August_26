class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += ord(num1[i]) - ord('0')
                i -= 1

            if j >= 0:
                total += ord(num2[j]) - ord('0')
                j -= 1

            res.append(chr(total % 10 + ord('0')))
            carry = total // 10

        return ''.join(res[::-1])
