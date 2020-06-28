class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for src, dest in tickets:
            if src in graph:
                graph[src].append(dest)
            else:
                graph[src] = [dest]

        for k in graph.keys():
            graph[k].sort(reverse=True)

        stack = res = []
        stack = ["JFK"]

        while len(stack) > 0:
            city = stack[-1]
            if city in graph and len(graph[city]) > 0:
                stack.append(graph[city].pop())
            else:
                res.append(stack.pop())

        return res[::-1]
