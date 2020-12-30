def part2() -> None:
    with open("input.txt") as infile:
        grid = infile.read().splitlines()

    rows = len(grid)
    cols = len(grid[0])

    #print(rows, cols)

    increments = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
        ]

    product = 1
    
    for right, down in increments:
        tree_count = 0
        row = 0
        col = 0
        while row < rows:
            if grid[row][col] == "#":
                tree_count += 1

            row += down
            col += right
            col %= cols

        product *= tree_count

    print(product)
            


part2()
