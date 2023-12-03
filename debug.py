import numpy as np
from linear_solvers import NumPyLinearSolver, HHL
matrix = np.array([ [1, -1/3], [-1/3, 1] ])
vector = np.array([1, 0])
naive_hhl_solution = HHL().solve(matrix, vector)