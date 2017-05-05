from random import randint
import math


class Decision:
    """This class represents a choice of move of AI"""

    def evaluate(self, grid):
        """Heuristic function to evaluate a grid (how good/bad a grid is to the winning state)"""
        weight = [[17, 9, 5, 3], [8, 4, 2, 0], [3, 1, 0, 0], [0, 0, 0, 0]]
        count = 0
        for i in range(grid.size):
            for j in range(grid.size):
                count += grid.tile[i][j] * weight[i][j]
        # Evaluation for a grid is based on its tiles, the number of empty tiles and number of monotonic rows or columns
        return count * 17 + len(grid.getAvailableTiles()) * 11 + self.monotonicity(grid) * 7

    def monotonicity(self, grid):
        """
        Check the monotonicity of rows and columns in a grid. Reward points for good monotonic rows or columns to use 
        later in heuristic function. Return the rewarded points of a grid 
        """
        reward = 0
        for i in range(grid.size):
            # Check the monotonicity of the rows
            currentList = []
            for j in range(grid.size):
                currentList.append(grid.getTile(i, j))
            if self.checkMonotone(currentList):
                reward += 1

            # Check the monotonicity of the columns
            currentList = []
            for j in range(grid.size):
                currentList.append(grid.getTile(j, i))
            if self.checkMonotone(currentList):
                reward += 1
        return reward

    def checkMonotone(self, aList):
        """Check if a list of numbers is monotonic"""
        monoDir = aList[1] - aList[0]
        for i in range(2, len(aList)):
            if (aList[i] - aList[i - 1]) * monoDir < 0:
                return False
        return True

    def getMove(self, state):
        """Run minimax algorithm and return the optimal move"""
        # Run minimax AI with depth of search 6, can change to other values based on the number of empty tiles in state
        if len(state.getAvailableTiles()) < 5:
            move = self.maximize(state, 0, - math.inf, math.inf, 6)[0]
        else:
            move = self.maximize(state, 0, - math.inf, math.inf, 6)[0]
        # Return best move found
        moves = state.getAvailableMoves()
        if move in moves:
            return move
        # If the optimal move is not available, random an available move
        return moves[randint(0, len(moves) - 1)]

    def minimize(self, state, maxMove, alpha, beta, depth):
        """Check all the possible insertions of a new tiles by the computer"""
        statecloneGrid = state.cloneGrid()
        minMove = None
        minUtil = math.inf
        for pos in state.getAvailableTiles():
            statecloneGrid.setTileValue(pos, 2)
            tempUtil = self.maximize(statecloneGrid, maxMove, alpha, beta, depth - 1)
            statecloneGrid.setTileValue(pos, 0)
            if tempUtil[1] < minUtil:
                minMove = tempUtil[0]
                minUtil = tempUtil[1]
            if minUtil <= alpha:
                break
            if minUtil < beta:
                beta = minUtil

        return minMove, minUtil

    def maximize(self, state, minMove, alpha, beta, depth):
        """Find the optimal move for AI"""
        if depth == 0:
            return minMove, self.evaluate(state)

        maxMove = None
        maxUtil = -math.inf

        for move in state.getAvailableMoves():
            statecloneGrid = state.cloneGrid()
            statecloneGrid.move(move)
            tempUtil = self.minimize(statecloneGrid, move, alpha, beta, depth - 1)[1]
            if tempUtil > maxUtil:
                maxMove = move
                maxUtil = tempUtil
            if maxUtil >= beta:
                break
            if maxUtil > alpha:
                alpha = maxUtil
        return maxMove, maxUtil
