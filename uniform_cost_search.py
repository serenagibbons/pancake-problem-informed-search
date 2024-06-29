class Node:
    """Node class for UCS pancake stack configurations"""

    def __init__(self, parent=None, pancakes=None):
        self.parent = parent
        self.pancakes = pancakes
        self.cost = 0
    
    def __eq__(self, other):
        return self.pancakes == other.pancakes

def flip(pancakes, i):
    """Flips the sublist of pancakes from index 0 to index i (inclusive)."""
    return pancakes[:i + 1][::-1] + pancakes[i + 1:]

def uniform_cost_search(pancakes):
    """
    Solves the pancake problem using the Uniform Cost Search algorithm.
    
    Returns the minimum number of flips, the number of nodes explored, and a list of pancake stack configurations that lead to the solution.
    """
    # create start node
    start_node = Node(None, pancakes)
    start_node.cost = 0

    # create end node
    end_pancakes = []
    for i in range(len(pancakes)):
        end_pancakes.append(i+ 1)
    end_node = Node(None, end_pancakes)
    end_node.cost = 0

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
        for index, node in enumerate(frontier):
            # find the node with the lowest cost
            if node.cost < current_node.cost:
                current_node = node
                current_index = index

        # pop current node off frontier and add to visted list
        frontier.pop(current_index)
        visited.append(current_node)

        # check if the current node is the end
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.pancakes)
                current = current.parent
            # return cost, number of nodes explored, and reversed path
            return current_node.cost, len(visited), path[::-1] 

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
            # set cost value
            child.cost = current_node.cost + 1

            # if child is not in frontier or visited
            if child not in frontier or child not in visited:
                frontier.append(child)
            # else if child is in frontier with higher cost
            else:
                for node in frontier:
                    if child == node and child.cost < node.cost:
                        # replace node in frontier with child
                        frontier.remove(node)
                        frontier.append(child)