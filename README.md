# Informed Search: The Pancake Problem

## A* Search Implementation 

### Total Function
The total function, f(n), is defined as the cost of the path (backward cost), g(n), plus the heurisitic to the goal (forward cost), h(n).
f(n) = g(n) + h(n)

### Cost Function
The Cost Function is used to calculate the backward cost of the path. The cost is calculated starting at 0, adding 1 every time a portion of the stack is flipped.

### Heuristic Function
The Gap Heuristic is used to estimate the forward cost to the goal. This heuristic counts the number of pancake stack positions for which the pancake at that position is not of adjacent size to the pancake below
