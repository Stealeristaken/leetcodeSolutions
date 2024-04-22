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



class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # bfs from target search
        # deadend elimite approach
        # use a visited to avoid duplicate
        # 0000 - [1000, 0100, 0010, 0001, 9000, 0900, 0090, 0009]

        if target == "0000":
            return 0
        if "0000" in (deadends := set(deadends)):
            return -1
        transitions = {str(i): (str((i + 1) % 10), str((i - 1) % 10)) for i in range(10)}
        start, end = {"0000"}, {target}
        deadends.add("0000")
        deadends.add(target)
        turns = 1
        while start and end:
            if len(start) > len(end):
                start, end = end, start
            temp = set()
            for state in start:
                for i in range(4):
                    for j in transitions[state[i]]:
                        new_state = state[:i] + j + state[i+1:]
                        if new_state in end:
                            return turns
                        if new_state not in deadends:
                            deadends.add(new_state)
                            temp.add(new_state)
            start = temp
            turns += 1
        return -1

        # visited = set()
        # for deadend in deadends:
        #     visited.add((int(deadend[0]), int(deadend[1]), int(deadend[2]), int(deadend[3])))
        # q = collections.deque([(0, 0, 0, 0, 0)])
        # t_a, t_b, t_c, t_d = int(target[0]), int(target[1]), int(target[2]), int(target[3])

        # while q:
        #     a,b,c,d,step = q.popleft()
        #     if (a, b, c, d) in visited or (a, b, c, d) in deadends:
        #         continue
        #     if a == t_a and b == t_b and c == t_c and d == t_d:
        #         return step

        #     visited.add((a, b, c, d))
        #     q.append(((a + 11) % 10, b, c, d, step + 1))
        #     q.append(((a + 9) % 10, b, c, d, step + 1))
        #     q.append((a, (b + 11) % 10, c, d, step + 1))
        #     q.append((a, (b + 9) % 10, c, d, step + 1))
        #     q.append((a, b, (c + 11) % 10, d, step + 1))
        #     q.append((a, b, (c + 9) % 10, d, step + 1))
        #     q.append((a, b, c, (d + 11) % 10, step + 1))
        #     q.append((a, b, c, (d + 9) % 10, step + 1))
            
        
        # return -1
