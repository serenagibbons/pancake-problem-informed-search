# Informed Search: The Pancake Problem

The pancake problem is a famous search problem where the objective is to sort a sequence of objects (pancakes) through a minimal number of prefix reversals (flips).

The goal is to sort the pancakes in the correct order with the largest on the bottom up to the smallest on top (e.g. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] where 1 is the smallest pancake and 10 is the largest pancake).

## Instructions
Run the program in the command line or terminal using the command `python main.py` in the root directory of the project.

The program prompts the user to enter the initial pancake stack and checks for valid input. After the pancake stack is initialized, the program displays a menu in the console prompting the user to select A* Search, Uniform Cost Search, or to terminate the program. The user may make a selection by typing the number corresponding to the option they would like to select, or `0` to terminate the program, and then pressing the `enter` key.

## A* Search Implementation 

### Total Function
The total function, f(n), is defined as the cost of the path (backward cost), g(n), plus the heurisitic to the goal (forward cost), h(n).

f(n) = g(n) + h(n)

### Cost Function
The Cost Function is used to calculate the backward cost of the path. The cost is calculated starting at 0, adding 1 every time a portion of the stack is flipped.

### Heuristic Function
The Gap Heuristic is used to estimate the forward cost to the goal. This heuristic counts the number of pancake stack positions for which the pancake at that position is not of adjacent size to the pancake below

## Uniform Cost Search Implementation

### Cost Function
The Cost Function is used to calculate the backward cost of the path. The cost is calculated starting at 0, adding 1 every time a portion of the stack is flipped.