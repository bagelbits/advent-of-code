dict1 = {}
list2 = []
similarity = 0

with open("input.txt") as f:
  for line in f:
    processed_line = line.rstrip().split('   ')
    dict1[int(processed_line[0])] = 0
    list2.append(int(processed_line[1]))

for i in list2:
  if i in dict1:
    dict1[i] += 1

for i in dict1:
  similarity += dict1[i] * i

print(similarity)
