from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0
        if target in deadends:
            return -1
        
        def get_next_states(state):
            for i in range(4):
                for d in [-1, 1]:
                    new_state = list(state)
                    new_state[i] = str((int(new_state[i]) + d) % 10)
                    yield ''.join(new_state)
        
        queue = deque(['0000'])
        visited = set(['0000'])
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                state = queue.popleft()
                for new_state in get_next_states(state):
                    if new_state in deadends or new_state in visited:
                        continue
                    if new_state == target:
                        return steps
                    visited.add(new_state)
                    queue.append(new_state)
        return -1
  
  
  
########################



