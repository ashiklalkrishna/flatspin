import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree

# Sample data
points = [(1, 2), (5, 3), (9, 6), (10,6),(3, 8), (6, 1)]
points = np.array(points)

# Build KDTree
tree = cKDTree(points)

plt.scatter(points[:,0], points[:,1])
# Query for nearest neighbors
query_point = (8,6)
distance_threshold = 2.0
nearest_neighbors_indices = tree.query_ball_point(query_point, distance_threshold)

print("Nearest neighbors indices:", nearest_neighbors_indices)
plt.show()

def neighbors(grid, i, a):
    tree = cKDTree(grid)

    query_point = grid[i]
    distance_threshold = a + 1e-5
    nearest_neighbors_indices = tree.query_ball_point(query_point, distance_threshold)
    nearest_neighbors_indices.remove(i)

    return nearest_neighbors_indices

N = 10
frac = 0.25
a = 1
grid = lattice(N, frac, a)

neighbour_list = neighbors(grid, 60, a)
print("Nearest neighbors indices:", neighbour_list)