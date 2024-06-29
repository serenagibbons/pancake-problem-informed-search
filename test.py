from a_star import a_star
from uniform_cost_search import uniform_cost_search

def test():
    test_cases = []
    # (pancakes, min flips)
    test_cases.append(([2,1,3], 1))
    test_cases.append(([3,2,1], 1))
    test_cases.append(([3,1,2,4], 2))
    test_cases.append(([4,2,1,3,5], 3))
    test_cases.append(([4,3,5,2,1], 3))
    test_cases.append(([1,2,5,3,4], 4))
    test_cases.append(([4,6,5,3,2,1], 3))
    test_cases.append(([5,4,6,2,1,3], 5))
    test_cases.append(([2,6,4,5,1,3], 6)) 
    test_cases.append(([1,2,3,7,6,5,4], 3))
    test_cases.append(([7,6,1,2,3,4,5,8,9], 2))
    test_cases.append(([2,3,4,5,8,9,1,6,7], 4))
    test_cases.append(([5,4,3,2,1,6,7,8,9,10], 1))
    test_cases.append(([1,2,5,4,3,6,7,8,9,10], 3))

    try:
        while test_cases:
            # pop the first test case
            pancakes, flips = test_cases.pop(0)

            # perform A* Search
            a_star_cost, a_star_explored, a_star_solution = a_star(pancakes)
            
            # perform Uniform Cost Search
            ucs_cost, ucs_explored, ucs_solution = uniform_cost_search(pancakes)

            # check if the cost for each algorithm is equal to the minimum number of flips
            success = a_star_cost == ucs_cost == flips
            result = "Pass" if success else "Fail"
            print(result + "\t" + str(pancakes))
    except KeyboardInterrupt:
        print("Terminating program.")

if __name__ == '__main__':
    test()