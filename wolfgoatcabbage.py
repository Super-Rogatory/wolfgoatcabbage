# Chukwudi Ikem
# For testing locally!
# Making the directory in aima-python available to reference
import sys
import os

sys.path.append(
    os.path.abspath("/home/super-rogatory/Desktop/Spring_2022/CPSC481/aima-python")
)
# For testing locally!

from search import *

# YOUR CODE GOES HERE
class WolfGoatCabbage(Problem):
    def __init__(self, initial={"F", "W", "G", "C"}, goal=set()):
        # Similar to EightPuzzle, we can define the initial and goal states for our problem.
        super().__init__(initial, goal)

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        return super().result(state, action)

    def actions(self, state):
        if state == {"F", "W", "G", "C"}:
            return [{"F", "G"}]
        elif state == {"W", "C"}:
            return [{"F", "G"}, {"F"}]
        elif state == {"F", "W", "C"}:
            return [{"F", "C"}, {"F", "W"}, {"F"}]


if __name__ == "__main__":
    wgc = WolfGoatCabbage()
    # solution = depth_first_graph_search(wgc).solution()
    # print(solution)
    # solution = breadth_first_graph_search(wgc).solution()
    # print(solution)
    print(wgc.actions())
