class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))

        directions = {
            'N': {-2: 'W', -1: 'E'},
            'E': {-2: 'N', -1: 'S'},
            'S': {-2: 'E', -1: 'W'},
            'W': {-2: 'S', -1: 'N'}
        }

        currX = currY = 0
        currDir = 'N'

        answer = 0

        for command in commands:
            if command < 0:
                currDir = directions[currDir][command]
                continue

            steps = command
            match currDir:
                case 'N':
                    while steps > 0 and (currX, currY + 1) not in obstacles:
                        currY += 1
                        steps -= 1
                case 'E':
                    while steps > 0 and (currX + 1, currY) not in obstacles:
                        currX += 1
                        steps -= 1
                case 'S':
                    while steps > 0 and (currX, currY - 1) not in obstacles:
                        currY -= 1
                        steps -= 1
                case 'W':
                    while steps > 0 and (currX - 1, currY) not in obstacles:
                        currX -= 1
                        steps -= 1

            answer = max(answer, (currX ** 2) + (currY ** 2))

        return answer