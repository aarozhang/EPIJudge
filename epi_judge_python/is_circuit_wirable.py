import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self) -> None:
        self.d = -1
        self.edges: List[GraphVertex] = []


def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    def bfs(v: GraphVertex) -> bool:
        v.d = 0
        q = collections.deque([v])

        while q:
            curr = q.popleft()
            for neighbor in curr.edges:
                if neighbor.d == -1:
                    neighbor.d = curr.d + 1
                    q.append(neighbor)
                elif curr.d == neighbor.d:
                    return False

        return True

    return all(bfs(vertex) for vertex in graph if vertex.d == -1)


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_circuit_wirable.py',
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
