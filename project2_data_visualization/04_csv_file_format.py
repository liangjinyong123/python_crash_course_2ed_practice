##### Chapter 16 Downolad Data #####
# The CSV File Format
## Parsing the CSV File Headers
from asyncore import read
from pathlib import Path
import csv
from turtle import color

import matplotlib.pyplot as plt
from datetime import datetime

from pyparsing import col

# path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)
# print(header_row)

## Printing the Headers and Their Positions
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

## Extracting and Reading Data
# highs = []
# for row in reader:
#     high = int(row[4])
#     highs.append(high)

# print(highs)

# ## Plotting Data in a Temperature Chart
# # Plot the high temperatures.
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(highs, color='red')

# # Format plot.
# ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()

## The datetime Module
# first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')
# print(first_date)

## Plotting Dates
# Extract dates and high temperatures.
# dates, highs = [], []
# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d')
#     high = int(row[4])
#     dates.append(current_date)
#     highs.append(high)

# # Plot the high temperatures.
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red')

# # Format plot.
# ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()

## Plotting a Longer Timeframe
# path = Path('weather_data/sitka_weather_2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# dates, highs = [], []
# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d')
#     dates.append(current_date)
#     high = int(row[4])
#     highs.append(high)

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red')

# # Format plot.
# ax.set_title("Daily High Temperatures, 2021", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()

## Plotting a Second Data Series
# path = Path('weather_data/sitka_weather_2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# dates, highs, lows = [], [], []
# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d')
#     high = int(row[4])
#     low = int(row[5])
#     dates.append(current_date)
#     highs.append(high)
#     lows.append(low)

# # Plot the high and low temperatures.
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red')
# ax.plot(dates, lows, color='blue')

# # Format plot.
# ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()

## Shading an Area in the Chart
# path = Path('weather_data/sitka_weather_2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# dates, highs, lows = [], [], []
# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d')
#     high = int(row[4])
#     low = int(row[5])
#     dates.append(current_date)
#     highs.append(high)
#     lows.append(low)

# # Plot the high and low temperatures.
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red', alpha=0.5)
# ax.plot(dates, lows, color='blue', alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# # Format plot.
# ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()

## Error Checking
path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

## Downloading your Own Data