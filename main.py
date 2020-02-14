path = "NewYorkTemps.txt"
content = open(path, "r")
read = content.readline()
count = 1
total = 0
condition = []
condition.append(read)

while read:
  read = content.readline()
  if read != '':
    condition.append(read)
    count += 1

for i in range(0, (count)):
  condition[i] = condition[i].replace("\n", "")

for x in range(0, count):
  condition[x] = float(condition[x])
  total = condition[x] + total

avrg = round((total / count), 3)
print(str(avrg))