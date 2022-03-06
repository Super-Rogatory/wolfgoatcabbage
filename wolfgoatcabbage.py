# Chukwudi Ikem
# TODO: Sititng at 15/25. So far everything has been brute force | take break | continue later tonight.

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
    def __init__(self, initial={"F", "W", "G", "C"}, goal=frozenset()):
        # Similar to EightPuzzle, we can define the initial and goal states for our problem.
        super().__init__(initial, goal)

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        if state == {"F", "W", "G", "C"} and action == {"F", "G"}:
            return {"W", "C"}
        elif state == {"W"} and action == {"F", "C"}:
            return {"F", "W", "C"}

    def actions(self, state):
        # mirroring possible_actions list from eight_sliding_puzzle.
        possible_actions = [{"F", "G"}, {"F"}, {"F", "C"}, {"F", "W"}]
        if state == {"F", "W", "G", "C"}:
            possible_actions = [elem for elem in possible_actions if elem == {"F", "G"}]
        elif state == {"W", "C"}:
            possible_actions = [
                elem for elem in possible_actions if elem == {"F", "G"} or elem == {"F"}
            ]
        elif state == {"F", "W", "C"}:
            possible_actions.remove({"F", "G"})
        return possible_actions


if __name__ == "__main__":
    wgc = WolfGoatCabbage()
    # solution = depth_first_graph_search(wgc).solution()
    # print(solution)
    # solution = breadth_first_graph_search(wgc).solution()
    # print(solution)
    print(wgc.actions())
