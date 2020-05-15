"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""

import csv

with open('texts.csv', 'r') as f:
    texts = list(csv.reader(f))

with open('calls.csv', 'r') as f:
    calls = list(csv.reader(f))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

from collections import defaultdict
import pdb

timeDict = dict()
for call in calls:
    timeDict[call[0]] = timeDict.get(call[0], 0) + int(call[3])
    timeDict[call[1]] = timeDict.get(call[1], 0) + int(call[3])

max_time = max(timeDict, key=lambda x: timeDict[x])
print(f"{max_time} spent the longest time, {timeDict[max_time]} seconds, on the phone during September 2016.")
