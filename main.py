from a_star import a_star

def main():
  # initialize pancake stack
  pancakes = [1,2,3,7,6,5,4] #pass
#   pancakes = [4,6,5,3,2,1] #pass
#   pancakes = [1,2,5,3,4] #pass
#   pancakes = [4,3,5,2,1] #pass
#   pancakes = [4,2,1,3,5] #pass
#   pancakes = [3,1,2,4] #pass
#   pancakes = [3,2,1] #pass
#   pancakes = [2,1,3] #pass

  # perform A* search
  cost, solution = a_star(pancakes)
  print("Complete.")
  print(f"Minimum flips required: {cost}")
  print(f"Solution path: {solution}")

if __name__ == '__main__':
    main()