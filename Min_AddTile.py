class Decision:
    # Find the child state with lowest utility value
    def minimize(self, state, alpha, beta):
        # return {"state": state, "util": util}
        if self.terminal_test(state):
            return None, self.evaluate(state)
        minChild = None
        minUtil = float("inf")
        for child in state.children():
            util = self.maximize(child, alpha, beta)
            if util < minUtil:
                minChild = child
                minUtil = util
            if minUtil <= alpha:
                break
            if minUtil < beta:
                beta = minUtil
        return {"minChild": minChild, "minUtil": minUtil}

    def terminal_test(self, state):
        return

    # Find the child state with highest utility value
    def maximize(self, state, alpha, beta):
        # return {"state": state, "util": util}
        if self.terminal_test(state):
            return None, self.evaluate(state)
        maxChild = None
        maxUtil = float("-inf")
        for child in state.children():
            util = self.minimize(child, alpha, beta)
            if util > maxUtil:
                maxChild = child
                maxUtil = util
            if maxUtil >= beta:
                break
            if maxUtil > alpha:
                alpha = maxUtil
        return {"maxChild": maxChild, "maxUtil": maxUtil}

    def evaluate(self, state):
        return 0

    def decision(self, state):
        child = self.maximize(state, float("-inf"), float("inf")["maxChild"])
        return child
