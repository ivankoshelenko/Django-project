import csv
import re

import numpy as np

name = "vacancies_with_skills.csv"
lines =[]
with open(name) as f:
    reader = csv.reader(f)
    for row in reader:
        lines.append(row)
header = lines[0]
del lines[0]
list =[]
for line in lines:
    if len(line) == len(header) and '' not in line:
        list.append(line)
print(header)
print(list)