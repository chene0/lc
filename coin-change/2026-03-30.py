class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        counts = [amount + 1] * (amount + 1)
        counts[0] = 0

        for coin in coins:
            for a in range(coin, amount + 1):
                counts[a] = min(counts[a], counts[a - coin] + 1)

        return counts[amount] if counts[amount] != amount + 1 else -1
