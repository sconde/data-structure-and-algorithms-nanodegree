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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


outgoingCalls = set( call[0] for call in calls)
incomingCalls = set( call[1] for call in calls)
outgoingText = set( text[0] for text in texts)
incomingText = set(text[1] for text in texts)

sorted_numbers = '\n'.join(list(sorted(outgoingCalls - (incomingCalls|outgoingText|incomingText))))
print(f"These numbers could be telemarketers: {sorted_numbers}")
