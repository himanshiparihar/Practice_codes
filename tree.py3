import sys, threading
from collections import deque, defaultdict
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
class TreeHeight:
        def read(self):
                self.n1 = int(sys.stdin.readline())
                self.parent1 = list(map(int, sys.stdin.readline().split()))
        def compute_height(self):
                nodes = defaultdict(set)
                for i1 in range(self.n1):
                    if self.parent1[i1] == -1: root = i1
                    else: nodes[self.parent1[i1]].add(i1)
                if nodes == None: return
                q, level, target, active= deque([root]), 0, root, 0
                while q:
                    node = q.popleft()
                    if node == target:
                        level, active = level + 1, 1
                    if nodes[node] != []:
                        for i1, child in enumerate(nodes[node]):
                            q.append(child)
                        if active == 1 and q:
                            target, active = q[-1], 0
                return level
def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())
threading.Thread(target = main).start()