class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
      task_map = [0]*26
      for task in tasks:
            task_map[ord(task) - ord('A')] += 1
      task_map.sort()
      max_val = task_map[25] - 1
      idle_slots = max_val * n
      for i in range(24, -1, -1):
            idle_slots -= min(task_map[i], max_val)
      return len(tasks) + max(0, idle_slots)





#############

from queue import PriorityQueue
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = Counter(tasks)
        return max((n+1)*(max(l.values())-1) + len([x for x in l.values() if x == max(l.values())]) , len(tasks))
        