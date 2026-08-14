class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted(
            (query, i) for i, query in enumerate(queries)
        )

        freq = [0] * (n + 1)
        ans = [0] * len(queries)

        left = 0
        right = 0
        active_servers = 0

        for query, index in sorted_queries:

            while right < len(logs) and logs[right][1] <= query:
                server = logs[right][0]

                if freq[server] == 0:
                    active_servers += 1

                freq[server] += 1
                right += 1

            while left < right and logs[left][1] < query - x:
                server = logs[left][0]

                freq[server] -= 1

                if freq[server] == 0:
                    active_servers -= 1

                left += 1

            ans[index] = n - active_servers

        return ans
