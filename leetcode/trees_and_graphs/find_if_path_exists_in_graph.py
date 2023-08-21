from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        current_search = []

        for i, edge in enumerate(edges):
            if source in edge:
                current_search = edges.pop(i)
