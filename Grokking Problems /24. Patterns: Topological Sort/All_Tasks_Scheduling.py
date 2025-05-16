'''
Problem Statement #
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: There is only possible ordering of the tasks.
Example 2:

Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
Output: 
1) [3, 2, 0, 1]
2) [3, 2, 1, 0]
Explanation: There are two possible orderings of the tasks meeting all prerequisites.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: 
1) [0, 1, 4, 3, 2, 5]
2) [0, 1, 3, 4, 2, 5]
3) [0, 1, 3, 2, 4, 5]
4) [0, 1, 3, 2, 5, 4]
5) [1, 0, 3, 4, 2, 5]
6) [1, 0, 3, 2, 4, 5]
7) [1, 0, 3, 2, 5, 4]
8) [1, 0, 4, 3, 2, 5]
9) [1, 3, 0, 2, 4, 5]
10) [1, 3, 0, 2, 5, 4]
11) [1, 3, 0, 4, 2, 5]
12) [1, 3, 2, 0, 5, 4]
13) [1, 3, 2, 0, 4, 5]
'''
from collections import defaultdict
from collections import deque

def printAllTaskOrders(numTasks, prerequisites):
    graph = defaultdict(list)
    indegree = {i: 0 for i in range(numTasks)}

    for parent, child in prerequisites:
        graph[parent].append(child)
        indegree[child] += 1

    all_orders = []

    def backtrack(current_order, visited, indegree):
        if len(current_order) == numTasks:
            all_orders.append(list(current_order))
            return

        for node in range(numTasks):
            if indegree[node] == 0 and node not in visited:
                # Choose
                visited.add(node)
                current_order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1

                # Explore
                backtrack(current_order, visited, indegree)

                # Unchoose (Backtrack)
                visited.remove(node)
                current_order.pop()
                for neighbor in graph[node]:
                    indegree[neighbor] += 1

    backtrack([], set(), indegree.copy())

    for idx, order in enumerate(all_orders):
        print(f"{idx+1}) {order}")


printAllTaskOrders(3, [[0, 1], [1, 2]])
print("-------------------")
printAllTaskOrders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
