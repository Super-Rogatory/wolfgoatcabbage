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
    def __init__(self, initial=frozenset({"F", "W", "G", "C"}), goal=frozenset()):
        # Similar to EightPuzzle, we can define the initial and goal states for our problem.
        super().__init__(initial, goal)

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        new_result = set(state)
        # TODO: fix result function.
        # possible_actions = [{"F"}, {"F", "C"}, {"F", "G"}, {"F", "W"}]
        if action == "F":
            if "F" in new_result:
                new_result.remove("F")
            else:
                new_result.add("F")

        elif action == {"F", "C"}:
            if "F" in new_result:
                new_result.remove("F")
                new_result.remove("G")
            else:
                new_result.add("F")
                new_result.add("C")

        elif action == {"F", "G"}:
            if "F" in new_result:
                new_result.remove("F")
                new_result.remove("G")
            else:
                new_result.add("F")
                new_result.add("G")

        elif action == {"F", "W"}:
            if "F" in new_result:
                new_result.remove("F")
                new_result.remove("W")
            new_result.add("F")
            new_result.add("W")

        return frozenset(new_result)  # unhashable type error if result is not frozen

    def actions(self, state):
        # mirroring possible_actions list from eight_sliding_puzzle. acknowledge bidrectional potential.
        # include left and right hand states when possible.
        possible_actions = []
        if state == {"F", "W", "G", "C"}:
            # farmer goat is the only way to start (move must be correct)
            possible_actions = [{"F", "G"}]
        elif state == {"W", "C"} or state == {"F", "G"}:
            # if we are in state cw, we can move the farmer back or move the farmer and goat back. also present with fg.
            possible_actions = [{"F", "G"}, {"F"}]
        elif state == {"F", "W", "C"} or state == {"G"}:
            # can move farmer, farmer cabbage, farmer wolf.
            possible_actions = [{"F"}, {"F", "C"}, {"F", "W"}]
        elif state == {"W"} or state == {"G", "C", "F"}:
            # F,G to go forward, F,W to go backward
            possible_actions = [{"F", "G"}, {"F", "C"}]
        elif state == {"C"} or state == {"G", "W", "F"}:
            # F,G to go forward, F,C to go backward
            possible_actions = [{"F", "G"}, {"F", "W"}]

        return possible_actions


if __name__ == "__main__":
    wgc = WolfGoatCabbage()
    print(wgc.result({"W"}, {"F", "C"}))
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
