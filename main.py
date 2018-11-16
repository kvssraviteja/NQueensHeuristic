from heuristic import heuristic_attcked_cells, heuristic_free_cells, no_heuristic, heuristic_random, create_board
from agent import  NQueensAgent


def print_board(board):
    for i in board:
        print(i)

def main():

    agent = NQueensAgent(heuristic_free_cells, 8)
    result, places = agent.solve()
    print(result, places, agent.num_of_calls())
    #board = create_board(places, 8)
    #print_board(board)

    agent2 = NQueensAgent(heuristic_attcked_cells, 8)
    result, places = agent2.solve()
    print(result, places, agent2.num_of_calls())

    agent3 = NQueensAgent(no_heuristic, 8)
    result, places = agent3.solve()
    print(result, places, agent3.num_of_calls())

    agent4 = NQueensAgent(heuristic_random, 8)
    result, places = agent4.solve()
    print(result, places, agent4.num_of_calls())


if __name__ == "__main__":
    main()