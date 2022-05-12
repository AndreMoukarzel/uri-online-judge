# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# -*- coding: utf-8 -*-

def input_as_matrix():
    N = int(input())
    matrix = []
    
    for i in range(N):
        row = []
        for col in map(int, input().split()):
            row.append(col)
        matrix.append(row)
    
    return matrix


def isBiGraph(matrix):
    colors = [-1] * len(matrix[0])
    colors[0] = 0
    queue = [0]
    
    while queue:
        u = queue.pop()
        
        for v in range(len(matrix[0])):
            # U and V cant communicate and V is not colored
            if matrix[u][v] == 0 and colors[v] == -1:
                colors[v] = 1 - colors[u]
                queue.append(v)
            elif matrix[u][v] == 0 and colors[v] == colors[u]:
                # U and V cant communicate and are in the same tank
                return False
    return True


"""
matrix = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1]
]
"""

matrix = [
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1]
]
if isBiGraph(matrix):
    print("Bazinga!")
else:
    print("Fail!")