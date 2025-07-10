import matplotlib.pyplot as plt
import numpy as np

# Constants
GRID_SIZE = 10   # 10x10 grid
CELL_SIZE = 1
ERASER_SIZE = 1  # size in cells

# Create a grid (1=blue, 0=erased)
grid = np.ones((GRID_SIZE, GRID_SIZE))

# Set up plot
fig, ax = plt.subplots()
canvas = ax.imshow(grid, cmap='Blues', extent=[0, GRID_SIZE, 0, GRID_SIZE])
ax.set_xticks(np.arange(0, GRID_SIZE + 1, 1))
ax.set_yticks(np.arange(0, GRID_SIZE + 1, 1))
ax.grid(which='both', color='gray', linewidth=1)
ax.set_title('Click and drag to erase')
plt.gca().invert_yaxis()

def erase_cell(event):
    if event.xdata is None or event.ydata is None:
        return

    col = int(event.xdata)
    row = int(event.ydata)

    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        # Erase a block of ERASER_SIZE x ERASER_SIZE cells
        for r in range(row, min(row + ERASER_SIZE, GRID_SIZE)):
            for c in range(col, min(col + ERASER_SIZE, GRID_SIZE)):
                grid[r, c] = 0  # Set to white (erased)

        canvas.set_data(grid)
        fig.canvas.draw_idle()

# Connect the mouse motion event
fig.canvas.mpl_connect('motion_notify_event', erase_cell)

plt.show()
