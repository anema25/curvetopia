# src/completion.py

def complete_curve(XY):
    # Simple linear interpolation to complete the curve
    if len(XY) < 2:
        return XY
    
    completed_curve = []
    for i in range(len(XY) - 1):
        completed_curve.append(XY[i])
        mid_point = (XY[i] + XY[i + 1]) / 2
        completed_curve.append(mid_point)
    completed_curve.append(XY[-1])
    
    return np.array(completed_curve)

# Example usage:
# XY = np.array([[0, 0], [1, 1], [2, 2]])
# completed_XY = complete_curve(XY)
# plot([completed_XY])
