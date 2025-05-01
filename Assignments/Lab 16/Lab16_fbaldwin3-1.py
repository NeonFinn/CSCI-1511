from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

FIRST_NAME = 0
LAST_NAME = 1
ATTENDANCE = 2
FAVORITE_LECTURE = 3

path = Path('names.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, attendance_count = [], []
for row in reader:
    current_date = datetime.strptime(row[FAVORITE_LECTURE], '%m/%d/%Y')
    dates.append(current_date)
    attendance = int(row[ATTENDANCE])
    attendance_count.append(attendance)


plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, attendance_count, c='blue')

ax.set_title('Attendance Count', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Attendance', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()



