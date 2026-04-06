class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pivot = 0
        tank = 0
        acc = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff
            acc += diff

            if tank < 0:
                pivot = i + 1
                tank = 0

        return pivot if acc >= 0 else -1
