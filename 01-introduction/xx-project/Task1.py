"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    texts = list(csv.reader(f))

with open('calls.csv', 'r') as f:
    calls = list(csv.reader(f))


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


numbers = set()

for text in texts:
    numbers.add(text[0])
    numbers.add(text[1])

for call in calls:
    numbers.add(call[0])
    numbers.add(call[1])

print(f"There are {len(numbers)} different telephone numbers in the records.")
