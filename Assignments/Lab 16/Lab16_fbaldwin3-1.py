from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# constants for columns
DATE = 0
OHUR = 1

# read the CSV file and split it into lines
path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

# skip the header row and create a reader object
reader = csv.reader(lines)
header_row = next(reader)

# try to read the data, print missing data if any
dates, ohur = [], []
for index, row in enumerate(reader):
    try:
        current_date = datetime.strptime(row[DATE], '%Y-%m-%d')
        current_ohur = float(row[OHUR])
    except ValueError:
        print(f"Missing data for {row[DATE]}")
    else:
        dates.append(current_date)
        ohur.append(current_ohur)

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, ohur)

ax.set_title('Ohio Unemployment Rates: 1976 - 2022', fontsize=16)
ax.set_xlabel('Date', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Unemployment Rate', fontsize=16)
ax.tick_params(labelsize=12)

plt.show()