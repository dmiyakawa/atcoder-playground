#!/usr/bin/env python3
#
# https://atcoder.jp/contests/typical90/tasks/typical90_c
#

import sys


class Node:
    def __init__(self, id):
        self.id = id
        self.score = 0
        self.links = set()

    def add_link(self, node):
        assert node not in self.links
        self.links.add(node)
        node.links.add(self)

    def __str__(self):
        return f"<id={self.id}, score={self.score} links=<{','.join(str(node.id) for node in self.links)}>>"

    __repr__ = __str__


def main():
    N = int(sys.stdin.readline())
    all_nodes = {}
    for i in range(N - 1):
        a_id, b_id = [int(e) for e in sys.stdin.readline().split()]
        node_a = all_nodes.setdefault(a_id, Node(a_id))
        node_b = all_nodes.setdefault(b_id, Node(b_id))
        node_a.add_link(node_b)

    edge_nodes = set()
    for node_id in range(1, N + 1):
        node = all_nodes[node_id]
        if len(node.links) == 1:
            edge_nodes.add(node)

    for i in range(N-2):
        node = edge_nodes.pop()
        assert len(node.links) == 1
        neighbor: Node = node.links.pop()
        neighbor.score = max(neighbor.score, node.score + 1)
        neighbor.links.remove(node)
        if len(neighbor.links) == 1:
            edge_nodes.add(neighbor)
    assert len(edge_nodes) == 2
    node_a = edge_nodes.pop()
    node_b = edge_nodes.pop()
    print(node_a.score + node_b.score + 2, end="")


if __name__ == "__main__":
    main()
