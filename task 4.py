def print_grid(grid):
    """Print the Sudoku grid."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(grid, row, col, num):
    """Check if it's valid to place `num` in `grid[row][col]`."""
    # Check if `num` is not in the current row
    if num in grid[row]:
        return False
    
    # Check if `num` is not in the current column
    if num in (grid[i][col] for i in range(9)):
        return False
    
    # Check if `num` is not in the current 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    
    return True

def find_empty_location(grid):
    """Find an empty location in the grid (represented by 0)."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def solve_sudoku(grid):
    """Solve the Sudoku puzzle using backtracking."""
    empty_loc = find_empty_location(grid)
    if not empty_loc:
        return True  # Puzzle solved
    
    row, col = empty_loc
    
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Backtrack

    return False

def main():
    # Example Sudoku puzzle (0 represents an empty cell)
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("Unsolved Sudoku Grid:")
    print_grid(sudoku_grid)
    
    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Grid:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
