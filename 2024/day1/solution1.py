list1 = []
list2 = []
total_distance = 0

with open("input.txt") as f:
  for line in f:
    processed_line = line.rstrip().split('   ')
    list1.append(int(processed_line[0]))
    list2.append(int(processed_line[1]))

list1.sort()
list2.sort()
for i in range(len(list1)):
  total_distance += abs(list1[i] - list2[i])

print(total_distance)
