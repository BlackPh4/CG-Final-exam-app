"""
For the Sweep Line Algorithm in the app we ll need to add the points and the grid for it in order to make it work
"""
import matplotlib
matplotlib.use("TkAgg")  #This create some visualisation issues

import numpy as np
import matplotlib.pyplot as plt


def find_largest_empty_square_sweep(points, grid_size):
    """
    Finds the largest empty square using the Sweep Line Algorithm.
    Ensures the square region is fully empty.
    """
    obstacles = set(points)
    max_size = 0
    best_corners = []

    # Sweep through each starting point (top-left of the square)
    for x in range(grid_size):
        for y in range(grid_size):
            if (x, y) in obstacles:
                continue  # Skip obstacle points

            # Determine the largest possible square from (x, y)
            possible_size = grid_size - max(x, y)  # Max possible size given grid limits
            for size in range(possible_size, 0, -1):  # Try the biggest first
                # Define square corners
                bottom_right = (x + size - 1, y + size - 1)

                # Check if square is fully empty
                is_valid = all(
                    (i, j) not in obstacles
                    for i in range(x, x + size)
                    for j in range(y, y + size)
                )

                if is_valid and size > max_size:
                    max_size = size
                    best_corners = [
                        (x, y),  # Top-left
                        (x + size - 1, y),  # Top-right
                        (x + size - 1, y + size - 1),  # Bottom-right
                        (x, y + size - 1)  # Bottom-left
                    ]
                    break  # Stop checking smaller squares

    return max_size, best_corners


def visualize_grid_sweep(points, grid_size, corners):

    fig, ax = plt.subplots()
    ax.set_xticks(range(grid_size))
    ax.set_yticks(range(grid_size))
    ax.grid(True)
    ax.invert_yaxis()
    ax.set_aspect('equal')

    # Plot obstacles
    for x, y in points:
        plt.scatter(x, y, c='red', marker='*')

    # Draw the largest empty square
    if corners:
        top_left, top_right, bottom_right, bottom_left = corners
        square_x = [top_left[0], top_right[0], bottom_right[0], bottom_left[0], top_left[0]]
        square_y = [top_left[1], top_right[1], bottom_right[1], bottom_left[1], top_left[1]]
        plt.plot(square_x, square_y, 'b-', linewidth=2)

    plt.savefig("sweep_line_output.png")
    plt.show()


# Example: Define obstacle points manually
points = [(60,60),(3, 5), (7, 12), (15, 8), (22, 27), (35, 16), (18, 30), (24, 6), (39, 39), (5, 19), (11, 25),   (29, 7), (2, 33), (14, 21), (9, 14), (31, 35), (26, 4), (38, 11), (19, 24), (12, 37), (1, 3),   (20, 5), (6, 8), (28, 18), (17, 23), (30, 12), (4, 28), (34, 31), (8, 2), (36, 10), (21, 26),   (13, 29), (23, 32), (16, 9), (32, 17), (37, 6), (27, 34), (10, 1), (0, 20), (25, 13), (33, 22),   (3, 7), (7, 35), (15, 19), (22, 15), (35, 26), (18, 1), (24, 39), (39, 3), (5, 30), (11, 9),   (29, 37), (2, 16), (14, 25), (9, 4), (31, 11), (26, 33), (38, 20), (19, 36), (12, 28), (1, 14),   (20, 32), (6, 22), (28, 5), (17, 18), (30, 29), (4, 23), (34, 12), (8, 38), (36, 8), (21, 6),   (13, 10), (23, 27), (16, 31), (32, 40), (37, 21), (27, 17), (10, 39), (0, 24), (25, 8), (33, 3),   (3, 11), (7, 28), (15, 34), (22, 9), (35, 14), (18, 20), (24, 26), (39, 12), (5, 1), (11, 6),   (29, 32), (2, 30), (14, 37), (9, 15), (31, 19), (26, 7), (38, 35), (19, 22), (12, 2), (1, 9)]


grid_size = 100  # Define a grid size

# Compute largest empty square using Sweep Line Algorithm
size, corners = find_largest_empty_square_sweep(points, grid_size)

# Output in console for corners of the square and the size of it
print(f"Largest Empty Square Size: {size}")
print(f"Corners: {corners}")

# Visualize the result
visualize_grid_sweep(points, grid_size, corners)
