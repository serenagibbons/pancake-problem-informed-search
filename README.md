# Informed Search: The Pancake Problem

The pancake problem is a famous search problem where the objective is to sort a sequence of objects (pancakes) through a minimal number of prefix reversals (flips).

The goal is to sort the pancakes in the correct order with the largest on the bottom up to the smallest on top (e.g. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] where 1 is the smallest pancake and 10 is the largest pancake).

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