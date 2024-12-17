puzzle = []

with open("input.txt") as f:
  for line in f:
    line = line.rstrip()
    puzzle.append(list(line))

xmas_count = 0
for i in range(1, len(puzzle) - 1):
  for j in range(1, len(puzzle[i]) - 1):
    if puzzle[i][j] == 'A':
      # M.M
      # .A.
      # S.S
      if (puzzle[i - 1][j - 1] == 'M' and puzzle[i + 1][j + 1] == 'S' and
          puzzle[i - 1][j + 1] == 'S' and puzzle[i + 1][j - 1] == 'M'):
        xmas_count += 1
      # S.M
      # .A.
      # S.M
      elif (puzzle[i - 1][j - 1] == 'S' and puzzle[i + 1][j + 1] == 'M' and
            puzzle[i - 1][j + 1] == 'M' and puzzle[i + 1][j - 1] == 'S'):
        xmas_count += 1
      # S.S
      # .A.
      # M.M
      elif (puzzle[i - 1][j - 1] == 'S' and puzzle[i + 1][j + 1] == 'M' and
            puzzle[i - 1][j + 1] == 'S' and puzzle[i + 1][j - 1] == 'M'):
        xmas_count += 1
      # M.S
      # .A.
      # M.S
      elif (puzzle[i - 1][j - 1] == 'M' and puzzle[i + 1][j + 1] == 'S' and
            puzzle[i - 1][j + 1] == 'M' and puzzle[i + 1][j - 1] == 'S'):
        xmas_count += 1

print(xmas_count)
