# src/symmetry.py

def is_symmetric(XY):
    # Assume vertical symmetry for simplicity
    center_x = np.mean(XY[:, 0])
    left_side = XY[XY[:, 0] < center_x]
    right_side = XY[XY[:, 0] > center_x]
    
    if len(left_side) != len(right_side):
        return False
    
    # Check if each point on the left side mirrors a point on the right side
    for left_point in left_side:
        mirrored_point = [2 * center_x - left_point[0], left_point[1]]
        if not any(np.allclose(mirrored_point, right_side_point) for right_side_point in right_side):
            return False
    return True

# Example usage:
# XY = np.array([[1, 2], [0, 1], [-1, 2]])
# print(is_symmetric(XY))
