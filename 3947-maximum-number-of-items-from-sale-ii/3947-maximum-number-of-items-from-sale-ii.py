class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        gain = [0] * (n + 1)

        for factor in range(1, n + 1):
            total = 0

            for multiple in range(factor, n + 1, factor):
                total += freq[multiple]

            gain[factor] = total - 1

        offers = []

        for factor, price in items:
            if gain[factor] > 0:
                offers.append((price, 2, gain[factor]))

            offers.append((price, 1, float('inf')))

        def compare(a, b):
            p1, v1, _ = a
            p2, v2, _ = b

            left = v1 * p2
            right = v2 * p1

            if left != right:
                return -1 if left > right else 1

            return -1 if p1 < p2 else (1 if p1 > p2 else 0)

        offers.sort(key=cmp_to_key(compare))

        answer = 0

        for price, value, count in offers:
            if budget < price:
                continue

            if value == 2:
                bought = min(count, budget // price)
            else:
                bought = budget // price

            answer += bought * value
            budget -= bought * price

            if value == 1:
                break

        return answer
