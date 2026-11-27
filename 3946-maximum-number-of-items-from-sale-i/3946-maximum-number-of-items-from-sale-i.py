
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        groups = {}

        for i, (factor, price) in enumerate(items):
            free = 0

            for j, (other, _) in enumerate(items):
                if i != j and other % factor == 0:
                    free += 1

            groups.setdefault(price, []).append(free + 1)

        dp = [-1] * (budget + 1)
        dp[0] = 0

        answer = 0

        for price in sorted(groups, reverse=True):
            current = [-1] * (budget + 1)

            for benefit in groups[price]:
                for cost in range(budget, price - 1, -1):

                    if dp[cost - price] != -1:
                        current[cost] = max(
                            current[cost],
                            dp[cost - price] + benefit
                        )

                    if current[cost - price] != -1:
                        current[cost] = max(
                            current[cost],
                            current[cost - price] + benefit
                        )

                    dp[cost] = max(
                        dp[cost],
                        dp[cost - price] + benefit
                    )

            for cost in range(budget + 1):
                if current[cost] != -1:
                    extra = (budget - cost) // price
                    answer = max(
                        answer,
                        current[cost] + extra
                    )

        return answer
