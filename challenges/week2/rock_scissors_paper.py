import sys


def get_winner(value_1, value_2):
    if value_1 == "R" and value_2 == "S" or value_1 == "S" and value_2 == "R":
        return "R"
    elif value_1 == "R" and value_2 == "P" or value_1 == "P" and value_2 == "R":
        return "P"
    elif value_1 == "P" and value_2 == "S" or value_1 == "S" and value_2 == "P":
        return "S"
    else:
        return value_1


def get_new_state(grid, r, c, rows, cols):
    if rows == 1 and cols > 1:
        if c == 0:
            winner = get_winner(grid[r][c], grid[r][c+1])
            return winner
        elif c == cols-1:
            winner = get_winner(grid[r][c], grid[r][c-1])
            return winner
        else:
            winner = get_winner(grid[r][c], grid[r][c-1])
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c+1]))
            return winner
    elif cols == 1 and rows > 1:
        if r == 0:
            winner = get_winner(grid[r][c], grid[r+1][c])
            return winner
        elif r == rows-1:
            winner = get_winner(grid[r][c], grid[r-1][c])
            return winner
        else:
            winner = get_winner(grid[r][c], grid[r-1][c])
            winner = get_winner(winner, get_winner(grid[r][c], grid[r+1][c]))
            return winner

    if 0 < r < rows-1:
        if 0 < c < cols-1:
            winner = get_winner(grid[r][c], grid[r-1][c])
            winner = get_winner(winner, get_winner(grid[r][c], grid[r+1][c]))
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c-1]))
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c+1]))
            return winner
        elif c == 0:
            winner = get_winner(grid[r][c], grid[r-1][c])
            winner = get_winner(winner, get_winner(grid[r][c], grid[r+1][c]))
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c+1]))
            return winner
        elif c == cols-1:
            winner = get_winner(grid[r][c], grid[r-1][c])
            winner = get_winner(winner, get_winner(grid[r][c], grid[r+1][c]))
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c-1]))
            return winner
    elif r == 0:
        if 0 < c < cols-1:
            winner = get_winner(grid[r][c], grid[r+1][c])
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c-1]))
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c+1]))
            return winner
        elif c == 0:
            winner = get_winner(grid[r][c], grid[r+1][c])
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c+1]))
            return winner
        elif c == cols-1:
            winner = get_winner(grid[r][c], grid[r+1][c])
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c-1]))
            return winner
    elif r == rows-1:
        if 0 < c < cols-1:
            winner = get_winner(grid[r][c], grid[r-1][c])
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c-1]))
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c+1]))
            return winner
        elif c == 0:
            winner = get_winner(grid[r][c], grid[r-1][c])
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c+1]))
            return winner
        elif c == cols-1:
            winner = get_winner(grid[r][c], grid[r-1][c])
            winner = get_winner(winner, get_winner(grid[r][c], grid[r][c-1]))
            return winner


with sys.stdin as stdin:
    t = int(stdin.readline())
    result = ""
    for i in range(t):
        rows, cols, n = map(int, stdin.readline().split())
        if rows == 0 or cols == 0:
            stdin.readline()
            print()
            continue

        grid = []
        for r in range(rows):
            grid.append(stdin.readline().strip())

        for day in range(n):
            new_grid = []
            for r in range(rows):
                new_grid.append("")
                for c in range(cols):
                    if rows > 1 or cols > 1:
                        new_grid[r] += get_new_state(grid, r, c, rows, cols)
                    else:
                        new_grid[r] += grid[r][c]

            grid = new_grid

        for r in range(rows):
            print(grid[r])

        print()
