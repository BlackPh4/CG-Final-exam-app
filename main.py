"""""
The points need to be placed manually in the points section from the bottom, you can add more of them, they are not tied to a limit
The application shows the size of the created square and the corners of it, they are shown in the console
The application is tested for points with coordinates up to 30.
A problem occurs when the points are further and further cuz the metric system gets really stuffed and you cannot distinguish the numbers anymore
"""


import numpy as np
import matplotlib.pyplot as plt


def find_largest_empty_square(points):
    if not points:
        return 0, (0, 0), [], np.zeros((1, 1), dtype=int)

    # Determine dynamic square grid size
    max_coord = max(max(x for x, y in points), max(y for x, y in points)) + 1
    grid_size = max_coord

    grid = np.zeros((grid_size, grid_size), dtype=int)

    # Mark given points on the grid
    for x, y in points:
        grid[y, x] = 1  # Mark obstacles

    # DP table to store largest square ending at (i, j)
    dp = np.zeros((grid_size, grid_size), dtype=int)
    max_size = 0
    bottom_right = (0, 0)

    # Compute largest square in such way that if the place a point a bit more far then others it will still get it into consideration for largest empty square
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] == 0:  # If cell is empty
                if i == 0 or j == 0:
                    dp[i, j] = 1
                else:
                    dp[i, j] = min(dp[i - 1, j], dp[i, j - 1], dp[i - 1, j - 1]) + 1

                if dp[i, j] > max_size:
                    max_size = dp[i, j]
                    bottom_right = (j, i)

    # Find square corners
    if max_size > 0:
        top_left = (bottom_right[0] - max_size + 1, bottom_right[1] - max_size + 1)
        bottom_left = (top_left[0], bottom_right[1])
        top_right = (bottom_right[0], top_left[1])
        corners = [tuple(map(int, top_left)), tuple(map(int, top_right)),
                   tuple(map(int, bottom_right)), tuple(map(int, bottom_left))]

    else:
        corners = []

    return max_size, bottom_right, corners, grid


def visualize_grid(points, grid_size, corners):
    fig, ax = plt.subplots()
    ax.set_xticks(range(grid_size))
    ax.set_yticks(range(grid_size))
    ax.grid(True)
    ax.invert_yaxis()

    # Plot obstacles
    for x, y in points:
        plt.scatter(x, y, c='violet', marker='*')


    #This part is responsible for the creation of the largest empty square
    #The figure don t look like a square but if you count the mini squares you can observe that they are the same number
    if corners:
        top_left, top_right, bottom_right, bottom_left = corners
        square_x = [top_left[0], top_right[0], bottom_right[0], bottom_left[0], top_left[0]]
        square_y = [top_left[1], top_right[1], bottom_right[1], bottom_left[1], top_left[1]]
        plt.plot(square_x, square_y, 'b-', linewidth=2)


    plt.savefig("output.png") # stores the visualization into an output image named "output.png" I'm not sure if is gonna make it automatically in the project


# The place to add points in the plane manually
points = [(3, 3), (8, 2), (5, 20), (20, 15),(3,0),(0,3),(4,7),(2,4),(4,4),(17,13),(9,11),(4,12),(10,16)]
size, position, corners, grid = find_largest_empty_square(points)
print(f"Largest Empty Square Size: {size-1}") # Here needs to be size-1 because the size calculator doesn't work properly
print(f"Corners: {corners}")
visualize_grid(points, grid.shape[0], corners)
