import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:

    WHITE, GRAY, BLACK = range(3)

    def __init__(self) -> None:
        self.color = GraphVertex.WHITE
        self.edges: List['GraphVertex'] = []


def is_deadlocked(graph: List[GraphVertex]) -> bool:
    def has_cycle(vertex: GraphVertex):
        if vertex.color == GraphVertex.GRAY:
            return True

        if vertex.color == GraphVertex.BLACK:
            return False

        vertex.color = GraphVertex.GRAY
        for neighbor in vertex.edges:
            if has_cycle(neighbor):
                return True

        return False

    for v in graph:
        if v.color == GraphVertex.WHITE and has_cycle(v):
            return True

    return False


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('deadlock_detection.py',
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
