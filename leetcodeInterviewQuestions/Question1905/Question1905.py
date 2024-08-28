class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.grid1 = grid1
        self.grid2 = grid2
        self.rownum = len(grid1)
        self.colnum = len(grid1[0])
        self.valid_island = True
        return self.count_subislands()
    
    def count_subislands(self) -> int:
        count = 0
        for i in range(self.rownum):
            for j in range(self.colnum):
                if self.grid2[i][j] == 1:
                    self.process_island(i, j)
                    if self.valid_island:
                        count += 1
                    self.valid_island = True
        return count
    
    def process_island(self, i: int, j: int) -> None:
        self.grid2[i][j] = 0
        if self.grid1[i][j] == 0:
            self.valid_island = False

        if i > 0 and self.grid2[i - 1][j] == 1:
            self.process_island(i - 1, j)
        if i < self.rownum - 1 and self.grid2[i + 1][j] == 1:
            self.process_island(i + 1, j)
        if j > 0 and self.grid2[i][j - 1] == 1:
            self.process_island(i, j - 1)
        if j < self.colnum - 1 and self.grid2[i][j + 1] == 1:
            self.process_island(i, j + 1)