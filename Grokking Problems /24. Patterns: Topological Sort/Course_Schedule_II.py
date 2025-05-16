'''
Problem Statement #
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite 
tasks which need to be completed before it can be scheduled. Given the number of tasks and a 
list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2] 
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: []
Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: [0 1 4 3 2 5] 
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5] 
'''
from collections import defaultdict
from collections import deque

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    
    q = deque([])
    for i, val in enumerate(indegree):
        if val == 0:
            q.append(i)

    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for pt in graph[node]:
            indegree[pt] -= 1
            if indegree[pt] == 0:
                q.append(pt)

    return result if len(result) == numCourses else []

numCourses=3
prerequisites=[0, 1], [1, 2]
print(canFinish(numCourses, prerequisites))

numCourses=3
prerequisites=[0, 1], [1, 2], [2, 0]
print(canFinish(numCourses, prerequisites))

numCourses=6
prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
print(canFinish(numCourses, prerequisites))
