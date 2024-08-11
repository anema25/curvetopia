# src/main.py

from curves import read_csv, plot
from regularization import regularize_curve
from symmetry import is_symmetric
from completion import complete_curve

def main():
    # Load and plot the initial data
    paths_XYs = read_csv('data/examples/isolated.csv')
    plot(paths_XYs)
    
    for i, XYs in enumerate(paths_XYs):
        for XY in XYs:
            shape = regularize_curve(XY)
            print(f"Shape {i+1}: {shape}")
            
            if is_symmetric(XY):
                print(f"Shape {i+1} is symmetric")
            else:
                print(f"Shape {i+1} is not symmetric")
                
            completed_XY = complete_curve(XY)
            print(f"Completed Curve for Shape {i+1}: {completed_XY}")
            plot([completed_XY])

if __name__ == "__main__":
    main()
