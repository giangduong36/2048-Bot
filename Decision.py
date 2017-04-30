from Grid import *
from random import randint
import math

class Decision:

    def evaluate(self, grid):
        count = 17 * grid.tile[0][0] + 9 * grid.tile[0][1] + 5 * grid.tile[0][2] + 3 * grid.tile[0][3]
        count += 8 * grid.tile[1][0] + 4 * grid.tile[1][1] + 2 * grid.tile[1][2]
        count += 3 * grid.tile[2][0] + 1 * grid.tile[2][1]
        return count

    def getNextMove(self, state):
        move = self.maximize(state, 0, - math.inf, math.inf, 6)[0]
        # return best move found
        moves = state.getAvailableMoves()
        if move in moves:
            return move
        return moves[randint(0, len(moves) - 1)]

    def minimize(self, state, maxMove, alpha, beta, depth):
        statecloneGrid = state.cloneGrid()
        minUtil = math.inf
        for pos in state.getAvailableTiles():
            statecloneGrid.setTileValue(pos, 2)
            tempUtil = self.maximize(statecloneGrid, maxMove, alpha, beta, depth - 1)
            statecloneGrid.setTileValue(pos, 0)
            if tempUtil[1] < minUtil:
                minUtil = tempUtil[1]
            if minUtil <= alpha:
                break
            if minUtil < beta:
                beta = minUtil
        return maxMove, minUtil

    def maximize(self, state, minMove, alpha, beta, depth):
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
