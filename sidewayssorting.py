def read_input():
    while True:
        R, C = map(int, input().split())
        if R == 0 and C == 0:
            break
        grid = [input() for _ in range(R)]
        yield R, C, grid

def transpose(grid):
    return [''.join(row[i] for row in grid) for i in range(len(grid[0]))]

def solve():
    first_case = True
    for R, C, grid in read_input():
        columns = transpose(grid)

        # Sort columns lexicographically, ignoring case
        columns_sorted = sorted(columns, key=lambda col: col.lower())

        # Rebuild the rows from sorted columns
        sorted_grid = [''.join(columns_sorted[j][i] for j in range(C)) for i in range(R)]

        if not first_case:
            print()  # Blank line between test cases
        else:
            first_case = False

        for row in sorted_grid:
            print(row)

if __name__ == "__main__":
    solve()