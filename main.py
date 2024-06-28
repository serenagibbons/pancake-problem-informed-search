from a_star import a_star
from uniform_cost_search import uniform_cost_search

def initialize_pancake_stack():
    pancakes = []
    valid = False
    while not valid:
        n = int(input("Enter the size of the pancake stack you would like to sort: "))
        print(f"For each pancake position, enter a number from 1 through {n}.")
        for i in range(n):
            pancake = int(input(f"Enter pancake for position {i+1}: "))
            pancakes.append(pancake)
        valid = check_pancake_stack(pancakes)
        if not valid:
            print("Please enter a valid pancake stack configuration.")
            pancakes = []
    return pancakes

def check_pancake_stack(pancakes):
    n = len(pancakes)
    seen = []
    
    for i in range(1, n+1):
        # check if pancakes has the element
        if not i in pancakes:
            return False
        # check if pancakes has duplicate elements
        elif i in seen:
            return False
        seen.append(i)

    return True

def select_search_algorithm():
    user_input = ""
    while user_input == "":
        print("**********************************************************")
        print("Search Algorithm Menu")
        print("1. A* Search")
        print("2. Uniform Cost Search")
        print("**********************************************************")
        try:
            user_input = int(input("Select an algorithm to sort the pancake stack or enter 0 to quit: "))
        except:
            user_input = ""
        print()

        if user_input != 1 and user_input != 2 and user_input != 0:
            print("Please select a valid response.")
            user_input = ""

    return user_input
    
def main():
    # initialize pancake stack
    # pancakes = [9,1,2,5,3,7,4,8,6,10] # pass/fail # min flips = 8
    # pancakes = [2,3,4,5,8,9,1,6,7] # pass # min flips = 4
    # pancakes = [7,6,1,2,3,4,5,8,9] # pass # min flips = 2
    # pancakes = [1,2,3,7,6,5,4] # pass # min flips = 3
    # pancakes = [4,6,5,3,2,1] # pass # min flips = 3
    # pancakes = [1,2,5,3,4] # pass # min flips = 4
    # pancakes = [4,3,5,2,1] # pass # min flips = 3
    # pancakes = [4,2,1,3,5] # pass # min flips = 3
    # pancakes = [3,1,2,4] # pass # min flips = 2
    # pancakes = [3,2,1] # pass # min flips = 1
    # pancakes = [2,1,3] # pass # min flips = 2
    pancakes = initialize_pancake_stack()
    print(f"Initial pancake stack: {pancakes}\r\n")

    # while True:
    #     search_option = select_search_algorithm()

    #     if search_option == 0:
    #         # terminate the program
    #         print("Program terminated.")
    #         return
    #     elif search_option == 1:
    #         # perform A* Search
    #         cost, explored, solution = a_star(pancakes)
    #         print("A* Search Complete.")
    #     elif search_option == 2:
    #         # perform Uniform Cost Search
    #         cost, explored, solution = uniform_cost_search(pancakes)
    #         print("Uniform Cost Search Complete.")
        
    #     print(f"Minimum flips required: {cost}")
    #     print(f"Number of nodes explored: {explored}")
    #     print(f"Solution path: {solution}")
    #     print()

if __name__ == '__main__':
    main()