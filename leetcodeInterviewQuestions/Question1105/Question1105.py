import math

class Solution:
    def minHeightShelves(self, books: List[List   [int]], shelfWidth: int) -> int:
        #return self.bfs(books, shelfWidth)
        return self.dfs(books, shelfWidth, 0, shelfWidth, 0, {})

    def bfs(self, books, shelf_width):
        # book, width_remaining, row_height
        queue = [(shelf_width - books[0][0], books[0][1], 0)]
        for b in range(1, len(books)):
            queue_size = len(queue)
            while queue_size > 0:
                queue_size -= 1
                current = queue.pop(0)
                if current[0] >= books[b][0]:
                    queue.append((current[0]-books[b][0], max(current[1], books[b][1]), current[2]))
                if current[0] < books[b][0] or books[b][1] > current[1]:
                    queue.append((shelf_width-books[b][0], books[b][1], current[2] + current[1]))
        min_height = math.inf
        for x in queue:
            min_height = min(min_height, x[1] + x[2])
        return min_height

    def dfs(self, books, shelf_width, row_height, width_remaining, j, memo):
        if j >= len(books):
            return row_height

        key =  str(j) + "," + str(width_remaining)
        if key in memo:  return memo[key]

        book = books[j]
        same_row, new_col = math.inf, math.inf

        # add to current row if space permits
        if width_remaining >= book[0]:
            same_row = self.dfs(books, shelf_width, max(row_height, book[1]), \
                                width_remaining - book[0], j+1, memo)
        
        # add to next row
        if width_remaining < book[0] or book[1] > row_height:
            new_col = self.dfs(books, shelf_width, book[1], \
                               shelf_width - book[0], j+1, memo) + row_height
        
        memo[key] = min(same_row, new_col)
        return memo[key]

        

        