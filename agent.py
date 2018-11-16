class NQueensAgent():

    def __init__(self, heuristic, n = 8):
        self.heuristic = heuristic
        self.n = n
        self.calls = 0

    def legal_move(self, queens):
        temp_queens = queens

        #if len(temp_queens) == 0:
        #   return True

        for i in range(len(temp_queens)):
            checks = map(lambda q: self.attack(queens[i], q), queens[i+1:])
            if any(checks):
                return False

        return True

    def solve(self):
        self.calls = 0
        return self._solve([])

    def _solve(self, queens):
        self.calls += 1

        num_of_queens = len(queens)

        if num_of_queens == self.n:
            return True, queens

        places = list(map(lambda i: (num_of_queens, i), range(self.n)))
        new_queens = list(map(lambda i: [i] + queens, places))

        heuristic_values = list(map(lambda i: self.heuristic(i, self.n), new_queens))
        moves = list(zip(heuristic_values, new_queens))
        moves.sort(reverse=True)
        #print(moves)

        for (i, j) in moves:
            if self.legal_move(j):
                #print('ok')
                result, places = self._solve(j)
                if result:
                    return result, places

        return False, None

    def num_of_calls(self):
        return self.calls

    @staticmethod
    def attack(q1, q2):
        x1, y1 = q1
        x2, y2 = q2
        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            return True
        else:
            return False



