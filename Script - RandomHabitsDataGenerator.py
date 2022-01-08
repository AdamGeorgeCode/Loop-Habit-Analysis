# RandomHabitsDataGenerator.py
# Programme creates random habit data in the same output format as the loop habit tracker app.

# import the relevant modules
from pathlib import Path
import pyinputplus as pyip
import datetime as dt
import pandas as pd
import random

print('Programme started')

# input folder path to save data output file
windowsFP = pyip.inputFilepath(prompt='Input folder path location to output file: \n', strip='"',
                               blank=False, mustExist=True)

# get windows file path
p = Path(windowsFP)

# get today's date for filepath name
tday = dt.datetime.today()
tday = tday.strftime('%Y-%m-%d')

# create full csv filepath
stem = f'RandomlyGeneratedHabitData - {tday}.csv'
csvfilepath = Path(p, stem)
print(csvfilepath)

print('Relevant file path created')

# input the number of habits to be created
numberofhabits = pyip.inputInt(prompt='Input the number (integer) of habits to be created: \n', greaterThan=0)

# create a list for storing the data produced by this programme
habitdata = []

# create header for the csv
header = ['Date']
for date in range(numberofhabits):
    habitnum = date + 1
    header.append(f"Habit {habitnum}")
habitdata.append(header)

# create a date range parameter for habits to monitor - first date being the 2021-01-01
e = dt.datetime.today()
s = dt.datetime(2021, 1, 1)
dr = pd.date_range(start=s, end=e, freq='D', )
dr = dr.format(formatter=lambda x: x.strftime('%Y-%m-%d'))
dr.reverse()

# create a loop that creates the relevant data for the programme
for date in dr:
    row = [date]
    for n in range(numberofhabits):
        rannum = random.choice([0, 2])  # pick a random value 0 or 2
        row.append(f'Entry(timestamp={date}, value={rannum})')  # use a f string to create string required
    habitdata.append(row)

# create an output file to save habit data in
outputFile = open(csvfilepath, 'w')

# converts the lists in habitdata into strings which are written to the output file
for i in habitdata:
    sentence = ','.join(i)
    sentence = sentence + ',\n'
    outputFile.write(sentence)

# output file is saved
outputFile.close()

print('Programme Complete')
