puzzle = []

with open("input.txt") as f:
  for line in f:
    line = line.rstrip()
    puzzle.append(list(line))

xmas_count = 0
for i in range(len(puzzle)):
  for j in range(len(puzzle[i])):
    # horizontal
    if j + 3 < len(puzzle[i]):
      if puzzle[i][j] == 'X' and puzzle[i][j + 1] == 'M' and puzzle[i][j + 2] == 'A' and puzzle[i][j + 3] == 'S':
        xmas_count += 1
      if puzzle[i][j] == 'S' and puzzle[i][j + 1] == 'A' and puzzle[i][j + 2] == 'M' and puzzle[i][j + 3] == 'X':
        xmas_count += 1
    # vertical
    if i + 3 < len(puzzle):
      if puzzle[i][j] == 'X' and puzzle[i + 1][j] == 'M' and puzzle[i + 2][j] == 'A' and puzzle[i + 3][j] == 'S':
        xmas_count += 1
      if puzzle[i][j] == 'S' and puzzle[i + 1][j] == 'A' and puzzle[i + 2][j] == 'M' and puzzle[i + 3][j] == 'X':
        xmas_count += 1
    # diagonal
    if i + 3 < len(puzzle) and j + 3 < len(puzzle[i]):
      if puzzle[i][j] == 'X' and puzzle[i + 1][j + 1] == 'M' and puzzle[i + 2][j + 2] == 'A' and puzzle[i + 3][j + 3] == 'S':
        xmas_count += 1
      if puzzle[i][j] == 'S' and puzzle[i + 1][j + 1] == 'A' and puzzle[i + 2][j + 2] == 'M' and puzzle[i + 3][j + 3] == 'X':
        xmas_count += 1
    # reverse diagonal
    if i + 3 < len(puzzle) and j - 3 >= 0:
        if puzzle[i][j] == 'X' and puzzle[i + 1][j - 1] == 'M' and puzzle[i + 2][j - 2] == 'A' and puzzle[i + 3][j - 3] == 'S':
            xmas_count += 1
        if puzzle[i][j] == 'S' and puzzle[i + 1][j - 1] == 'A' and puzzle[i + 2][j - 2] == 'M' and puzzle[i + 3][j - 3] == 'X':
            xmas_count += 1

print(xmas_count)
