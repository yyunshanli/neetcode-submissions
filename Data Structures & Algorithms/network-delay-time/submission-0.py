import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        frontier = (n + 1) * [float('inf')]
        frontier[k] = 0

        q = []

        # adjacency list

        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}

            graph[u][v] = w

        heap = [(0, k)]

        while heap:
            curr_dist, curr_node = heapq.heappop(heap)

            if curr_dist > frontier[curr_node]:
                continue
            for neighbor, weight in graph[curr_node].items():
                dist = weight + curr_dist
                if dist < frontier[neighbor]:
                    frontier[neighbor] = dist
                    heapq.heappush(heap, (dist, neighbor))
        res = max(frontier[1:])
        if res == float('inf'):
            return -1
        return res
