#!/usr/bin/env python3

import heapq
import sys


class Item:
    def __init__(self, item_id, scores):
        self.item_id = item_id
        self.scores = scores
        self.index = 0

    def current_score(self) -> int:
        return self.scores[self.index]

    def consume(self) -> int:
        score = self.scores[self.index]
        self.index += 1
        return score

    def fully_consumed(self) -> bool:
        return len(self.scores) == self.index

    def __lt__(self, other: "Item"):
        return -self.current_score() < -other.current_score()


def main():
    # N問の試験、K分
    N, K = [int(e) for e in sys.stdin.readline().split()]
    heap = []
    for i in range(N):
        a, b = [int(e) for e in sys.stdin.readline().split()]
        heap.append(Item(i, [b, a - b]))

    heapq.heapify(heap)

    total = 0
    for i in range(K):
        item = heapq.heappop(heap)
        score = item.consume()
        total += score
        if not item.fully_consumed():
            heapq.heappush(heap, item)

    print(total, end="")


if __name__ == "__main__":
    main()


