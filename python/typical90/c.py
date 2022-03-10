#!/usr/bin/env python3
#
# https://atcoder.jp/contests/typical90/tasks/typical90_c
#

import sys


class Node:
    def __init__(self, id):
        self.id = id
        self.links = set()

    def add_link(self, node):
        assert node not in self.links
        self.links.add(node)
        node.links.add(self)

    def __str__(self):
        return f"<id={self.id}, links=<{','.join(str(node.id) for node in self.links)}>>"

    __repr__ = __str__


def main():
    N = int(sys.stdin.readline())
    all_nodes = {}
    for i in range(N - 1):
        a_id, b_id = [int(e) for e in sys.stdin.readline().split()]
        node_a = all_nodes.setdefault(a_id, Node(a_id))
        node_b = all_nodes.setdefault(b_id, Node(b_id))
        node_a.add_link(node_b)
    print(all_nodes)

    resolved = set()
    unresolved = set(all_nodes)
    node = all_nodes[1]
    distances = {node.id: 0}
    furthest_node: Node = node
    while unresolved:
        next_node = None
        if distances[furthest_node.id] < distances[node.id]:
            furthest_node = node
        next_distance = distances[node.id] + 1
        for i, neighbor in enumerate(node.links):
            distances[neighbor.id] = next_distance
            if next_node is None and neighbor.id not in resolved:
                next_node = neighbor
        resolved.add(node.id)
        unresolved.remove(node.id)
        node = next_node
    print(distances)


if __name__ == "__main__":
    main()
