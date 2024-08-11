# src/regularization.py

import numpy as np

def is_straight_line(XY):
    # Check if all points are collinear
    vec = XY[1] - XY[0]
    for i in range(2, len(XY)):
        new_vec = XY[i] - XY[0]
        if not np.isclose(np.cross(vec, new_vec), 0):
            return False
    return True

def is_circle(XY):
    # Check if all points are equidistant from the center
    center = np.mean(XY, axis=0)
    distances = np.linalg.norm(XY - center, axis=1)
    return np.allclose(distances, distances[0])

def regularize_curve(XY):
    if is_straight_line(XY):
        return 'Straight Line'
    elif is_circle(XY):
        return 'Circle'
    else:
        return 'Unknown Shape'

# Example usage:
# XY = np.array([[0, 0], [1, 1], [2, 2]])
# print(regularize_curve(XY))
