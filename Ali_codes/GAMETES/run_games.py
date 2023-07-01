from NashEqFinder import *
from game import *
from generate_game import *
import datetime


# for SIZE in [5, 10, 20, 30, 50]:
for SIZE in [850, 925]:
# for SIZE in [100, 250, 400, 700, 1000]:
# for SIZE in [250]:
# for SIZE in [400]:
# for SIZE in [700]:
# for SIZE in [550]:
# for SIZE in [925]:
# for SIZE in [1000]:
# for SIZE in [5, 10, 20, 30, 50, 100, 250, 400, 700, 1000]:
# for SIZE in [1000]:
    print(f"\n\n\n\n\n\n-------- SIZE: {SIZE} --------")
    print(f"Time before setting the game: {datetime.datetime.now()}")
    game_name = f"{SIZE} strategies"
    players_names = ['row','column']
    players_strategies = {}
    strategies = ['S' + str(i) for i in range(1,SIZE+1)]
    players_strategies['row'] = strategies
    players_strategies['column'] = strategies
    payoff_matrix = {}
    print(f"Time before reading the matrix: {datetime.datetime.now()}")
    read_matrix(payoff_matrix, SIZE)
    
    # Define an instance of the game
    print(f"Time before setting the game object: {datetime.datetime.now()}")
    PD = game(game_name, players_names, players_strategies, payoff_matrix)
    # Define an instance of the NashEqFinder
    print(f"Time before setting the first NashEqFinder: {datetime.datetime.now()}")
    NashEqFinderInst = NashEqFinder(PD)
    # print(f"Time before running the first optlangRun: {datetime.datetime.now()}")
    # [Nash_equilibria,exit_flag, game_payoff_matrix] = NashEqFinderInst.optlangRun()
    # print(f"Time before running the first show_matrix: {datetime.datetime.now()}")
    # show_matrix(game_payoff_matrix, Nash_equilibria, players_strategies['row'], "Original Game called by optlangFindPure")
    # print("Nash_equilibria optlangFindPure = ", Nash_equilibria)

    # Pick a random pair of numbers
    i = random.randint(1, SIZE)
    j = random.randint(1, SIZE)

    print(f"Time before running newEquilibria: {datetime.datetime.now()}")
    NashEqFinderInst.newEquilibria(nasheq_cells=[(('row',f'S{i}'), ('column',f'S{j}'))], strategies=strategies)


# make it into CLI that takes in the size of the game as an argument




# # for the cloud 
# import argparse
# from NashEqFinder import *
# from game import *
# import datetime

# # read the payoff matrix from the file
# def read_matrix(payoff_matrix, SIZE):
#     print("Reading the payoff matrix from the file")
#     with open(f"matrices/payoff_matrix_{SIZE}.txt", "r") as f:
#         lines = f.readlines()
#         # print(len(lines))
#         # print(len(lines[0].split()))
#         for i in range(SIZE):
#             for j in range(SIZE):
#                 payoff_matrix[('row', f"S{i+1}"), ('column', f"S{j+1}")] = \
#                     {'row': int(lines[i].split()[2*j]), 'column': int(lines[i].split()[2*j+1])}
                
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--size", type=int, help="The size of the game.")
#     args = parser.parse_args()

#     print(f"\n\n\n\n\n\n-------- SIZE: {args.size} --------")
#     print(f"Time before setting the game: {datetime.datetime.now()}")
#     game_name = f"{args.size} strategies"
#     players_names = ['row','column']
#     players_strategies = {}
#     strategies = ['S' + str(i) for i in range(1,args.size+1)]
#     players_strategies['row'] = strategies
#     players_strategies['column'] = strategies
#     payoff_matrix = {}
#     print(f"Time before reading the matrix: {datetime.datetime.now()}")
#     read_matrix(payoff_matrix, args.size)
    
#     # Define an instance of the game
#     print(f"Time before setting the game object: {datetime.datetime.now()}")
#     PD = game(game_name, players_names, players_strategies, payoff_matrix)
#     # Define an instance of the NashEqFinder
#     print(f"Time before setting the first NashEqFinder: {datetime.datetime.now()}")
#     NashEqFinderInst = NashEqFinder(PD)
#     # print(f"Time before running the first optlangRun: {datetime.datetime.now()}")
#     # [Nash_equilibria,exit_flag, game_payoff_matrix] = NashEqFinderInst.optlangRun()
#     # print(f"Time before running the first show_matrix: {datetime.datetime.now()}")
#     # show_matrix(game_payoff_matrix, Nash_equilibria, players_strategies['row'], "Original Game called by optlangFindPure")
#     # print("Nash_equilibria optlangFindPure = ", Nash_equilibria)

#     # Pick a random pair of numbers
#     i = random.randint(1, args.size)
#     j = random.randint(1, args.size)

#     print(f"Time before running newEquilibria: {datetime.datetime.now()}")
#     NashEqFinderInst.newEquilibria(nasheq_cells=[(('row',f'S{i}'), ('column',f'S{j}'))], strategies=strategies)


# if __name__ == "__main__":
#     main()


# # for the cloud again but without making it into a CLI
# from NashEqFinder import *
# from game import *
# import datetime

# # read the payoff matrix from the file
# def read_matrix(payoff_matrix, SIZE):
#     print("Reading the payoff matrix from the file")
#     with open(f"matrices/payoff_matrix_{SIZE}.txt", "r") as f:
#         lines = f.readlines()
#         # print(len(lines))
#         # print(len(lines[0].split()))
#         for i in range(SIZE):
#             for j in range(SIZE):
#                 payoff_matrix[('row', f"S{i+1}"), ('column', f"S{j+1}")] = \
#                     {'row': int(lines[i].split()[2*j]), 'column': int(lines[i].split()[2*j+1])}
            
# for SIZE in [30]:
#     print(f"\n\n\n\n\n\n-------- SIZE: {SIZE} --------")
#     print(f"Time before setting the game: {datetime.datetime.now()}")
#     game_name = f"{SIZE} strategies"
#     players_names = ['row','column']
#     players_strategies = {}
#     strategies = ['S' + str(i) for i in range(1,SIZE+1)]
#     players_strategies['row'] = strategies
#     players_strategies['column'] = strategies
#     payoff_matrix = {}
#     print(f"Time before reading the matrix: {datetime.datetime.now()}")
#     read_matrix(payoff_matrix, SIZE)
    
#     # Define an instance of the game
#     print(f"Time before setting the game object: {datetime.datetime.now()}")
#     PD = game(game_name, players_names, players_strategies, payoff_matrix)
#     # Define an instance of the NashEqFinder
#     print(f"Time before setting the first NashEqFinder: {datetime.datetime.now()}")
#     NashEqFinderInst = NashEqFinder(PD)
#     # print(f"Time before running the first optlangRun: {datetime.datetime.now()}")
#     # [Nash_equilibria,exit_flag, game_payoff_matrix] = NashEqFinderInst.optlangRun()
#     # print(f"Time before running the first show_matrix: {datetime.datetime.now()}")
#     # show_matrix(game_payoff_matrix, Nash_equilibria, players_strategies['row'], "Original Game called by optlangFindPure")
#     # print("Nash_equilibria optlangFindPure = ", Nash_equilibria)

#     # Pick a random pair of numbers
#     i = random.randint(1, SIZE)
#     j = random.randint(1, SIZE)

#     print(f"Time before running newEquilibria: {datetime.datetime.now()}")
#     NashEqFinderInst.newEquilibria(nasheq_cells=[(('row',f'S{i}'), ('column',f'S{j}'))], strategies=strategies)