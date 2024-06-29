# Informed Search: The Pancake Problem

The pancake problem is a famous search problem where the objective is to sort a sequence of objects (pancakes) through a minimal number of prefix reversals (flips).

The goal is to sort the pancakes in the correct order with the largest on the bottom up to the smallest on top (e.g. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] where 1 is the smallest pancake and 10 is the largest pancake).

Search Problem:
- Initial state: the starting pancake stack configuration
- Actions: select the next node to visit based on priority (algorithm-dependent)
- Successor function: find the set of states reachable from the current state
- Goal test: check if the search algorithm found the final (sorted) pancake stack configuration
- Path cost function (algorithm-dependent): cumulative cost of the path (Uniform Cost Search) or cumulative cost of the path + heuristic to the goal (A* Search)

## Instructions
Run the program in the command line or terminal using the command `python main.py` in the root directory of the project.

The program prompts the user to enter the initial pancake stack and checks for valid input. After the pancake stack is initialized, the program displays a menu in the console, prompting the user to select an algorithm to sort the pancake stack: A* Search or Uniform Cost Search. The user may make a selection by typing the number corresponding to the option they would like to select, or `0` to terminate the program, and then pressing the `enter` key.

Once the pancake stack is initialized, the user can select an algorithm to sort the stack until the user terminates the program. To reinitialize the pancake stack, the program must be restarted.

## A* Search Implementation 
A* Search expands the cheapest node first using a priority queue where the priority is the backward cost + the forward cost of the node.

### Total Function
The total function, f(n), is defined as the cost of the path (backward cost), g(n), plus the heurisitic to the goal (forward cost), h(n).

f(n) = g(n) + h(n)

### Cost Function
The Cost Function is used to calculate the backward cost of the path. The cost is calculated starting at 0, adding 1 every time a portion of the stack is flipped.

### Heuristic Function
The Gap Heuristic is used to estimate the forward cost to the goal. This heuristic counts the number of pancake stack positions for which the pancake at that position is not of adjacent size to the pancake below.

## Uniform Cost Search Implementation
Uniform Cost Search (UCS) expands the cheapest node first using a priority queue where the priority is the cumulative (path) cost of the node.

### Cost Function
The Cost Function is used to calculate cumulative cost of the node. The cost is calculated starting at 0, adding 1 every time a portion of the stack is flipped.