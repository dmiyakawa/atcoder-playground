#!/usr/bin/env python3

class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = self if parent is None else parent


class UnionFindTree:
    def __init__(self):
        self._all_nodes = {}

    def make_set(self, value):
        assert value not in self._all_nodes
        self._all_nodes[value] = Node(value=value)

    def unite(self, value_1, value_2):
        rank_1 = 1
        node_1 = self._all_nodes[value_1]
        while node_1.parent != node_1:
            rank_1 += 1
            node_1 = node_1.parent

        rank_2 = 1
        node_2 = self._all_nodes[value_2]
        while node_2.parent != node_2:
            rank_2 += 1
            node_2 = node_2.parent
        if node_1.value != node_2.value:
            if rank_1 < rank_2:
                node_1.parent = node_2
            else:
                node_2.parent = node_1

    def is_same(self, value_1, value_2):
        nodes_to_reset_root_1 = set()
        node_1 = self._all_nodes[value_1]
        while node_1.parent != node_1:
            nodes_to_reset_root_1.add(node_1)
            node_1 = node_1.parent
        for n in nodes_to_reset_root_1:
            n.parent = node_1

        nodes_to_reset_root_2 = set()
        node_2 = self._all_nodes[value_2]
        while node_2.parent != node_2:
            nodes_to_reset_root_2.add(node_2)
            node_2 = node_2.parent
        for n in nodes_to_reset_root_2:
            n.parent = node_2

        ret = (node_1.value == node_2.value)

        return ret


def main():
    import sys

    N, M = [int(e) for e in sys.stdin.readline().split()]
    links = {}
    for i in range(M):
        a, b = [int(e) for e in sys.stdin.readline().split()]
        links.setdefault(a, set()).add(b)
    answers = [0]
    num_joints = 0
    tree = UnionFindTree()
    for i in range(N, 1, -1):
        tree.make_set(i)
        num_joints += 1
        for b in links.get(i, set()):
            if not tree.is_same(i, b):
                tree.unite(i, b)
                num_joints -= 1
        answers.append(num_joints)
    for answer in reversed(answers):
        print(answer)


if __name__ == "__main__":
    main()
