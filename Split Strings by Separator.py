class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []

        for word in words:
            for part in word.split(separator):
                if part:
                    ans.append(part)

        return ans
