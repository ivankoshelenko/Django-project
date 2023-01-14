import csv
import re
import sqlite3

import matplotlib
import numpy as np


currency_to_rub = {
    "AZN": 35.68,
    "BYR": 23.91,
    "EUR": 59.90,
    "GEL": 21.74,
    "KGS": 0.76,
    "KZT": 0.13,
    "RUR": 1,
    "UAH": 1.64,
    "USD": 60.66,
    "UZS": 0.0055,
}

def AddToDatabase(line):
    db = sqlite3.connect('testdb.sqlite3')
    sql = db.cursor()
    db.commit()
    sql.execute(f"INSERT INTO unfiltered VALUES(?,?,?,?,?)",(line[0],line[1],line[2],line[3],line[4]))
    db.commit()

def CurrencyConverter(line):
    for key in currency_to_rub:
        if key in line[4]:
            line[2]= line[2] * currency_to_rub[key]
    return line

name = 'vacancies_with_skills.csv'
lines =[]
with open(name,encoding= 'utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        lines.append(row)
header = lines[0]
del lines[0]
list =[]
years =[]

yearsAmount = {2015:0 , 2016:0, 2017:0, 2018:0,2019:0,2020:0,2021:0,2022:0}
yearsVacancies ={2015:0 , 2016:0, 2017:0, 2018:0,2019:0,2020:0,2021:0,2022:0}
skillsArr = []
for line in lines:
     if len(line) == len(header) and '' not in line and ('fullstack' in line[1] or 'fullstack' in line[1]
                                                        or 'фулстак' in line[1] or 'фуллтак' in line[1] or 'фуллстэк' in line[1] or 'фулстэк' in line[1] or 'full stack' in line[1] or
                                                        'fullstack' in line[0] or 'fullstack' in line[0]
                                                        or 'фулстак' in line[0] or 'фуллтак' in line[0] or 'фуллстэк' in
                                                        line[0] or 'фулстэк' in line[0] or 'full stack' in line[0]):
        # if len(line) == len(header) and '' not in line:
        line[6] = line[6][0:4]
        line[2] = (float(line[2]) + float(line[3])) / 2
        if line[4]!='RUR':
            line = CurrencyConverter(line)
        skills = line[1]
        skills = skills.split("\n")
        for skill in skills:
            if skill not in skillsArr:
                skillsArr.append(skill)
        list.append(line)
        for year in yearsAmount:
            if int(line[6]) == year:
                yearsAmount[year] += line[2]

        for year in yearsVacancies:
            if int(line[6]) == year:
                yearsVacancies[year] += 1


print(yearsAmount)
print(yearsVacancies)
print(list)
for i in range(2015,2023):
    yearsAmount[i] = yearsAmount[i] / yearsVacancies[i]
print(yearsAmount)
        #AddToDatabase(line)

print(len(list))


