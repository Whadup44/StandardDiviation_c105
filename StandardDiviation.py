import math
import csv
with open('class1.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x[1])
    mean = total / n
    return mean
squaredList = []
for number in file_data:
    a = int(number[1]) - int(mean(file_data))
    a = a**2
    squaredList.append(a)
sum = 0
for i in squaredList:
    sum = sum + i
result = sum / (len(file_data) - 1)
standardDeviation = math.sqrt(result)
print(standardDeviation)