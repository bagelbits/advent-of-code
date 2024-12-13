safe = 0

def test_safety(report):
    is_safe = True
    prev = int(report[0])
    is_increase = None

    for i in range(1, len(report)):
      curr = int(report[i])
      if is_increase is None:
        if curr > prev:
          is_increase = True
        elif curr < prev:
          is_increase = False
        else:
          is_safe = False
          break

      if is_increase and curr < prev:
        is_safe = False
        break
      if not is_increase and curr > prev:
        is_safe = False
        break
      if abs(curr - prev) < 1 or abs(curr - prev) > 3:
        is_safe = False
        break
      prev = curr

    return is_safe


with open("input.txt") as f:
  for line in f:
    report = line.rstrip().split(' ')
    if test_safety(report):
      safe += 1
    else:
      for i in range(0, len(report)):
        new_report = report.copy()
        new_report.pop(i)
        if test_safety(new_report):
          safe += 1
          break

print(safe)
