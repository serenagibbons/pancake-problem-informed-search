from a_star import a_star
from uniform_cost_search import uniform_cost_search

def main():
  # initialize pancake stack
  pancakes = [2,3,4,5,8,9,1,6,7] # pass # min flips = 4
#   pancakes = [7,6,1,2,3,4,5,8,9] # pass # min flips = 2
#   pancakes = [1,2,3,7,6,5,4] # pass # min flips = 3
#   pancakes = [4,6,5,3,2,1] # pass # min flips = 3
#   pancakes = [1,2,5,3,4] # pass # min flips = 4
#   pancakes = [4,3,5,2,1] # pass # min flips = 3
#   pancakes = [4,2,1,3,5] # pass # min flips = 3
#   pancakes = [3,1,2,4] # pass # min flips = 2
#   pancakes = [3,2,1] # pass # min flips = 1
#   pancakes = [2,1,3] # pass # min flips = 2

  # perform A* Search
  cost, solution = a_star(pancakes)
  print("A* Search Complete.")
  print(f"Minimum flips required: {cost}")
  print(f"Solution path: {solution}")

  print()
  
  # perform Uniform Cost Search
  cost, solution = uniform_cost_search(pancakes)
  print("Uniform Cost Search Complete.")
  print(f"Minimum flips required: {cost}")
  print(f"Solution path: {solution}")

if __name__ == '__main__':
    main()