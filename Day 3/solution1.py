def part1() -> None:
    with open("input.txt") as infile:
        lines = infile.read().splitlines()

    row_length = len(lines[0])
    tree_count = 0
    
    for row, line in enumerate(lines):
        col = (row * 3) % row_length
        if line[col] == '#':
            tree_count += 1

    print(tree_count)

part1()
