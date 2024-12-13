import re

total = 0

with open("input.txt") as f:
  do = True  # Reset `do` flag for each line
  for line in f:
    mul_regexp = re.compile(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))")
    line = line.rstrip()
    mul = mul_regexp.findall(line)
    for m in mul:
      if m == "do()":
        do = True
        continue
      elif m == "don't()":
        do = False
        continue

      if do:
        m = m.replace('mul(', '')
        m = m.replace(')', '')
        m = m.split(',')
        product = int(m[0]) * int(m[1])
        total += product

print(f"Total: {total}")
