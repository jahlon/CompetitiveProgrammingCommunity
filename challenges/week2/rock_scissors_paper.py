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


with sys.stdin as stdin:
    t = int(stdin.readline())
    for i in range(t):
        rows, cols, n = map(int, stdin.readline().split())
        if rows == 0 or cols == 0:
            stdin.readline()
            print()
            continue

        grid = []
        for r in range(rows):
            grid.append(stdin.readline().strip())

        diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for day in range(n):
            new_grid = []
            for r in range(rows):
                new_grid.append("")
                for c in range(cols):
                    if rows > 1 or cols > 1:
                        res = ""
                        for d in diff:
                            if r + d[0] < 0 or r + d[0] >= rows or c + d[1] < 0 or c + d[1] >= cols:
                                continue

                            winner = get_winner(grid[r][c], grid[r + d[0]][c + d[1]])

                            if winner not in res:
                                res += winner

                        if len(res) > 1:
                            winner = get_winner(res[0], res[1])
                        else:
                            winner = res[0]

                        new_grid[r] += winner
                    else:
                        new_grid[r] += grid[r][c]

            grid = new_grid

        for r in range(rows):
            print(grid[r])

        if i < t-1:
            print()
