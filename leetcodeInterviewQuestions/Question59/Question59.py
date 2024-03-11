'''
Initially I wanted to do some smart mathy solution but then I realized I'm not getting any younger,
 so I decided to do a brute force method.

Approach:
I imaged a mouse trapped inside a box going in a circle clockwise but pooping as it's crawling.
When it walks head on into its own feces, it turns right.
This slow and smelly entrapment eventually ends after it drops n*n feces.
Rather than checking that it's trapped on all 4 direction, it will recall the number of feces it has dropped and give up.
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        direction = 1
        count = 1
        matrix = [[0 for i in range(n)] for j in range(n)]
        x,y = 0,0
        while count < n**2:
            while x < n - 1 and matrix[y][x+direction] == 0:
                matrix[y][x] = count
                count += 1
                x += direction
            matrix[y][x], matrix[y + direction][x] = count, count + 1
            count += 1
            y += direction
            while y < n - 1 and matrix[y+direction][x] == 0:
                matrix[y][x] = count
                count += 1
                y += direction
            matrix[y][x], matrix[y][x - direction] = count, count + 1
            count += 1
            x -= direction
            direction *= -1
        return matrix