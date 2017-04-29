from Grid import *
from random import randint
import math

class Decision:

    def evaluate(self, grid):
        count = 17 * grid.tile[0][0] + 9 * grid.tile[0][1] + 5 * grid.tile[0][2] + 3 * grid.tile[0][3]
        count += 8 * grid.tile[1][0] + 4 * grid.tile[1][1] + 2 * grid.tile[1][2]
        count += 3 * grid.tile[2][0] + 1 * grid.tile[2][1]
        return count
        # return state.getMaxTile()

    def getNextMove(self, state):
        move = self.maximize(state, -math.inf, - math.inf, math.inf, depth=4)[0]
        # return best move found
        moves = state.getAvailableMoves()
        if move in moves:
            return move
        return moves[randint(0, len(moves) - 1)]

    def minimize(self, state, maxMove, alpha, beta, depth):
        stateClone = state.cloneGrid()
        result = (None,math.inf)
        minMove = None
        minUtil = math.inf
        for pos in state.getAvailableTiles():
            stateClone.insertTile(pos, 2)
            tempUtil = self.maximize(stateClone, maxMove, alpha, beta, depth - 1)
            stateClone.setTileValue(pos, 0)
            if tempUtil[1] < minUtil:
                minMove = tempUtil[0]
                minUtil = tempUtil[1]
            if minUtil <= alpha:
                break
            if minUtil < beta:
                beta = minUtil
        return minMove, minUtil

    def maximize(self, state, minMove, alpha, beta, depth):
        if depth == 0:
            return self.evaluate(state), minMove

        result = (None, -math.inf)
        maxMove = result[0]
        maxUtil = result[1]
        stateClone = state.cloneGrid()
        for move in stateClone.getAvailableMoves():
            stateClone.move(move)
            tempUtil = self.minimize(stateClone, move, alpha, beta, depth - 1)[1]
            if tempUtil > maxUtil:
                maxMove = move
                maxUtil = tempUtil
            if maxUtil >= beta:
                break
            if maxUtil > alpha:
                alpha = maxUtil
        return maxMove, maxUtil


# initialization: alpha = -inf, beta = inf
# x = Grid()
#
# y = Decision()
# print(y.evaluate(x))
