class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        heap = [(-count, ch) for ch, count in freq.items()]
        heapq.heapify(heap)

        res = []
        prev = (0, "")

        while heap:
            count, ch = heapq.heappop(heap)
            res.append(ch)
            count += 1  # Since count is negative

            if prev[0] < 0:
                heapq.heappush(heap, prev)

            prev = (count, ch)

        return "".join(res) if len(res) == len(s) else ""
