import re

total = 0

with open("input.txt") as f:
  for line in f:
    mul_regexp = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    line = line.rstrip()
    mul = mul_regexp.findall(line)
    for m in mul:
      m = m.replace('mul(', '')
      m = m.replace(')', '')
      m = m.split(',')
      total += int(m[0]) * int(m[1])

print(total)
