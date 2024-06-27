from heapq import heappush, heappop

def flip(pancakes, i):
  """Flips the sublist of pancakes from index 0 to index i (inclusive)."""
  return pancakes[:i + 1][::-1] + pancakes[i + 1:]

def is_sorted(pancakes):
  """Check if the pancakes are sorted in ascending order."""
  return all(pancakes[i] <= pancakes[i + 1] for i in range(len(pancakes) - 1))

def gap_heuristic(pancakes):
  """Gap Heuristic: Count the number of pancake stack positions for which 
  the pancake at that position is not of adjacent size to the pancake below."""
  gap = 0
  for i in range(len(pancakes) - 1):
    if abs(pancakes[i] - pancakes[i + 1]) > 1:
      gap += 1
  return gap

def a_star(pancakes):
  """Solve the pancake problem using the A* search algorithm."""
  cost = 0
  gap = gap_heuristic(pancakes)
  estimated_cost = cost + gap
  frontier = [(estimated_cost, cost, pancakes)]  # (total cost, pancake configuration)
  visited = []

  while frontier:
    # for i in range(len(frontier)):
    #   print(frontier[i])
    estimated_cost, cost, current_state = heappop(frontier)
    print("current cost: " + str(cost))
    print("current state: " + str(current_state))
    print()

    # if we already visited the current pancake state, continue
    if current_state in visited:
    #   print("visited")
      continue

    # add current_state to visited list
    visited.append(current_state)

    if is_sorted(current_state):
      return cost, current_state

    # get possible pancake stack states and gap heuristics
    for i in range(1, len(current_state)):      
      next_state = flip(current_state.copy(), i)
      new_cost = cost + 1 
      new_gap = gap_heuristic(next_state)
      heappush(frontier, (new_cost + new_gap, new_cost, next_state))
  
  return cost, current_state