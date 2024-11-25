class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Flatten the board into a string
        solvedState = '123450'
        state =''
        # Flatten and create a string of the current board state
        for row in board:
            for num in row:
                state+=str(num)        
        # BFS setup. Queue should track board state and number of moves to get to this state
        queue = deque([(state, 0, state.index('0'))])  # Queue stores (state, moves, zeroIndex)
        visited = set()

        
        # Valid moves for each position on a 2x3 board
        # For example, if zero is at index 0 of the string, it can swap with the number at index 1 or index 3
        availableMoves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }
        # Iterate while there is something left in the queue
        while queue:
            board, moves, zeroIndex = queue.popleft()  # Dequeue the next state
            if board == solvedState:
                return moves  # Found the solution
            
            # Find the index of 0 (empty space) and generate neighbors
            for swap in availableMoves[zeroIndex]:
                newState = list(board)
                # Swap 0 with its neighbor
                newState[zeroIndex], newState[swap] = newState[swap], newState[zeroIndex]
                newState = ''.join(newState)  # Convert back to string
                
                # Check if this board state has been explored already, if it hasn't, add to queue and add to visited
                if newState not in visited:
                    visited.add(newState)  # Mark as visited
                    queue.append((newState, moves + 1, swap))  # Enqueue the new state
        
        return -1  # No solution