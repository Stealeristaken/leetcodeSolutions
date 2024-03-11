import copy


class Solution:
    NINE = [str(i + 1) for i in range(9)]
    NOTFILLED = 81

    def doneTest(self):
        self.NOTFILLED -= 1
        if self.NOTFILLED == 0:
            return True
        else:
            return False

    def nine(self, x):
        if x != ".":
            return [x]
        else:
            return Solution.NINE.copy()

    def removes(self, p, board):
        foundOne = True
        while foundOne:
            foundOne = False

            for i in range(9):
                for j in range(9):
                    array = p[i][j]
                    if len(array) == 1:
                        element = array[0]
                    else:
                        continue
                    board[i][j] = element
                    foundOne = True

                    for row in p[:][i]:
                        if element in row:
                            row.remove(element)

                    for col in [z[j] for z in p]:
                        if element in col:
                            col.remove(element)

                    r = 3 * (i // 3)
                    c = 3 * (j // 3)

                    for row in range(r, r + 3):
                        for col in range(c, c + 3):
                            if element in p[row][col]:
                                p[row][col].remove(element)

                    print("Found one")
                    if self.doneTest():
                        return p, board
        return p, board

    def dubTest(self, p, board):
        for i in range(9):
            for j in range(9):
                array = p[i][j]
                if array == []:
                    continue
                row = []
                col = []
                box = []
                for k in range(9):
                    if k != j:
                        row += p[i][k]
                    if k != i:
                        col += p[k][j]

                r = 3 * (i // 3)
                c = 3 * (j // 3)
                for z in range(r, r + 3):
                    for x in range(c, c + 3):
                        if z != i or x != j:
                            box += p[z][x]

                for element in array:
                    if element not in row:
                        p[i][j] = [element]
                        print("Found one ROW")
                        break

                    if element not in col:
                        p[i][j] = [element]
                        print("Found one COL")
                        break

                    if element not in box:
                        p[i][j] = [element]
                        print("Found one BOX")
                        break
        return p, board

    def groupTest(self, p, board):
        for i in range(9):
            for j in range(9):
                array = []
                a = p[i][j].copy()  # PROBLEM MED AT COPY

                for c in a:
                    array.append(copy)

                if array == []:
                    continue

                array = array.copy()

                count = 1
                match = [j]
                for rows in enumerate(p[:][i]):
                    if rows[0] != j and rows[1] == array:
                        count += 1
                        match.append(rows[0])
                        if count == len(array):
                            print("")
                            for element in array.copy():
                                for row in p[i]:
                                    if element in row:
                                        row.remove(element)
                            for m in match:
                                p[i][m] = array

                count = 1
                match = [i]
                for cols in enumerate([z[j] for z in p]):
                    if cols[0] != i and cols[1] == array:
                        count += 1
                        match.append(cols[0])
                        if count == len(array):
                            print("")
                            for element in array.copy():
                                for col in [z[j] for z in p]:
                                    if element in col:
                                        col.remove(element)  # DEN FUCKER HER VED AT SLETTE I ARRAY
                            for m in match:
                                p[m][j] = array

                count = 1
                match = [[i, j]]
                r = 3 * (i // 3)
                c = 3 * (j // 3)
                for z in range(r, r + 3):
                    for x in range(c, c + 3):
                        if z != i and x != j and array == p[z][x]:
                            count += 1
                            match.append([z, x])
                            if count == len(array):
                                print("")
                                for row in range(r, r + 3):
                                    for col in range(c, c + 3):
                                        for element in array.copy():
                                            if element in p[row][col]:
                                                p[row][col].remove(element)
                                for m in match:
                                    p[m[0]][m[1]] = array

        return p, board

    def validTest(self, p, board):
        boxes = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        for i in range(9):
            row = []
            col = []
            box = []

            for f in p[i] + board[i]:
                row += f

            for f in [z[i] for z in p]:
                col += f
            for f in [z[i] for z in board]:
                col += f

            r = 3 * (boxes[i][0] // 3)
            c = 3 * (boxes[i][1] // 3)
            for z in range(r, r + 3):
                for x in range(c, c + 3):
                    box += p[z][x] + [board[z][x]]

            for number in range(1, 10):
                if str(number) not in row:
                    return False
                if str(number) not in col:
                    return False
                if str(number) not in box:
                    return False
        return True

    def geuss(self, p, board):
        langde = 9
        # giver OOB hvis fejl
        I = 10
        J = 10
        for i in range(9):
            for j in range(9):
                array = p[i][j].copy()
                if len(array) < langde:
                    I = i
                    J = j

                if array == [] or len(array) != 2:
                    continue

                for rows in enumerate(p[:][i]):
                    if rows[0] != j and rows[1] == array:
                        for geuss in array:
                            boardCopy = copy.deepcopy(board)
                            boardCopy[i][j] = geuss
                            boolean, boardCopy = Solution()._solveSudoku(boardCopy)
                            if boolean:
                                board = copy.deepcopy(boardCopy)
                                return p, board

                for cols in enumerate([z[j] for z in p]):
                    if cols[0] != i and cols[1] == array:
                        for geuss in array:
                            boardCopy = copy.deepcopy(board)
                            boardCopy[i][j] = geuss
                            boolean, boardCopy = Solution()._solveSudoku(boardCopy)
                            if boolean:
                                board = copy.deepcopy(boardCopy)
                                return p, board

                r = 3 * (i // 3)
                c = 3 * (j // 3)
                for z in range(r, r + 3):
                    for x in range(c, c + 3):
                        if z != i and x != j and array == p[z][x]:
                            for geuss in array:
                                boardCopy = copy.deepcopy(board)
                                boardCopy[i][j] = geuss
                                boolean, boardCopy = Solution()._solveSudoku(boardCopy)
                                if boolean:
                                    board = copy.deepcopy(boardCopy)
                                    return p, board

        for array in p[I][J]:
            for geuss in array:
                boardCopy = copy.deepcopy(board)
                boardCopy[i][j] = geuss
                boolean, boardCopy = Solution()._solveSudoku(boardCopy)
                if boolean:
                    board = copy.deepcopy(boardCopy)
                    return p, board

        return p, board

    def compare(self, p, pCopy):
        for i in range(9):
            for j in range(9):
                if p[i][j] != pCopy[i][j]:
                    return False
        return True

    def _solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        p = [[self.nine(board[j][i]) for i in range(9)] for j in range(9)]
        if self.NOTFILLED == 0:
            return p, board

        p, board = self.removes(p, board)
        while self.NOTFILLED > 0:
            print(self.validTest(p, board))
            if not self.validTest(p, board):
                return False, board

            pCopy = copy.deepcopy(p)
            p, board = self.dubTest(p, board)
            p, board = self.removes(p, board)
            p, board = self.groupTest(p, board)
            p, board = self.removes(p, board)
            if self.compare(p, pCopy):
                print("geussing")
                p, board = self.geuss(p, board)
                return self.validTest(p, board), board

        print(self.NOTFILLED)
        return True, board

    def solveSudoku(self, board: list[list[str]]) -> None:
        _, boardAns = self._solveSudoku(board)
        for i in range(9):
            for j in range(9):
                board[i][j] = boardAns[i][j]