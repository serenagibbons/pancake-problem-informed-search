from heapq import heappush, heappop

def flip(pancakes, i):
  """Flips the sublist of pancakes from index 0 to index i (inclusive)."""
  return pancakes[:i + 1][::-1] + pancakes[i + 1:]

def is_sorted(pancakes):
  """Check if the pancakes are sorted in ascending order."""
  return all(pancakes[i] <= pancakes[i + 1] for i in range(len(pancakes) - 1))

def uniform_cost_search(pancakes):
  """Solve the pancake problem using the A* search algorithm."""
  cost = 0
  frontier = [(cost, pancakes)]  # (total cost, pancake configuration)
  visited = []

  while frontier:
    # for i in range(len(frontier)):
    #   print(frontier[i])
    cost, current_state = heappop(frontier)
    # print("current cost: " + str(cost))
    # print("current state: " + str(current_state))
    # print()

    # if we already visited the current pancake state, continue
    if current_state in visited:
      continue

    # add current_state to visited list
    visited.append(current_state)

    if is_sorted(current_state):
      return cost, current_state

    # get possible pancake stack states
    for i in range(1, len(current_state)):      
      next_state = flip(current_state.copy(), i)
      new_cost = cost + 1 
      heappush(frontier, (new_cost, next_state))
  
  return cost, current_state