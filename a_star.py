class Node:
    """Node class for A* Search pancake stack configurations"""

    def __init__(self, parent=None, pancakes=None):
        self.parent = parent
        self.pancakes = pancakes

        self.f = 0
        self.g = 0
        self.h = 0
    
    def __eq__(self, other):
        return self.pancakes == other.pancakes

def flip(pancakes, i):
    """Flips the sublist of pancakes from index 0 to index i (inclusive)."""
    return pancakes[:i + 1][::-1] + pancakes[i + 1:]

def gap_heuristic(pancakes):
    """Gap Heuristic: Count the number of pancake stack positions for which 
    the pancake at that position is not of adjacent size to the pancake below."""
    gap = 0
    for i in range(len(pancakes) - 1):
        if abs(pancakes[i] - pancakes[i + 1]) > 1:
            gap += 1
    return gap

def a_star(pancakes):
    """
    Solves the pancake problem using the A* Search algorithm.
    
    Returns the minimum number of flips, the number of nodes explored, and a list of pancake stack configurations that lead to the solution.
    """
    # create start node
    start_node = Node(None, pancakes)
    start_node.g = start_node.h = start_node.f = 0

    # create end node
    end_pancakes = []
    for i in range(len(pancakes)):
        end_pancakes.append(i+ 1)
    end_node = Node(None, end_pancakes)
    end_node.g = end_node.h = end_node.f = 0

    # initialize frontier and visited nodes list
    frontier = []
    visited = []

    # add start node to the frontier
    frontier.append(start_node)

    # search the frontier
    while len(frontier) > 0:

        # get the current node
        current_node = frontier[0]
        current_index = 0
        for index, item in enumerate(frontier):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # pop current off frontier and add to visted list
        frontier.pop(current_index)
        visited.append(current_node)

        # check if the current node is the end
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.pancakes)
                current = current.parent
            # return cost and reversed path
            return current_node.g, len(visited), path[::-1] 

        # generate children pancake stack configurations
        children = []
        for i in range(1, len(current_node.pancakes)):      
           next_state = flip(current_node.pancakes.copy(), i)
           # create new node
           new_node = Node(pancakes=next_state, parent=current_node)
           # add to children list
           children.append(new_node)

        # iterate through children
        for child in children:
            # child is on the visited list
            for visited_child in visited:
                if child == visited_child:
                    continue

            # set f, g, and h values
            child.g = current_node.g + 1
            child.h = gap_heuristic(child.pancakes)
            child.f = child.g + child.h

            # child is already in the frontier
            for node in frontier:
                if child == node and child.g > node.g:
                    continue

            # aa the child to the frontier
            frontier.append(child)