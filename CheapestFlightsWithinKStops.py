class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        if src == dst:
            return 0

        d = collections.defaultdict(list)
        seen = collections.defaultdict(lambda: float("inf"))

        for u, v, p in flights:
            d[u] += [(v, p)]

        q = collections.deque([(src, -1, 0)])

        while q:
            pos, k, cost = q.popleft()
            if pos == dst or k == K:
                continue
            else:
                for nei, price in d[pos]:
                    if cost + price >= seen[nei]:
                        continue
                    else:
                        seen[nei] = cost + price
                        q += [(nei, k + 1, cost + price)]

        return seen[dst] if seen[dst] < float("inf") else -1

