class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        p = len(costs)
        costs_ = sorted(costs, key=lambda cost: abs(
            cost[0] - cost[1]), reverse=True)

        a, b = [], []
        for l in costs_:
            if len(a) != p / 2 and len(b) != p / 2:
                if l[0] < l[1]:
                    a.append(l[0])
                else:
                    b.append(l[1])
            else:
                if len(a) != p / 2:
                    a.append(l[0])
                else:
                    b.append(l[1])

        total = sum(a) + sum(b)
        return total
