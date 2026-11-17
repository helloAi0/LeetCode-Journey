class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                for d in range(1, length):
                    if length % d != 0:
                        continue
                    changes = 0
                    for offset in range(d):
                        left = start + offset
                        right = start + length - d + offset
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    cost[start][start + length - 1] = min(cost[start][start + length - 1], changes)
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for parts in range(1, k + 1):
            for end in range(2* parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    dp[parts][end] = min(dp[parts][end], dp[parts - 1][start] + cost[start][end - 1])
        return dp[k][n]