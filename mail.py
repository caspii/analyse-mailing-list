import mailbox
from dateutil import parser
import sys


if len(sys.argv) < 2:
    print("You need to supply an mbox filename")
    sys.exit()

mbox_name = sys.argv[1]
mbox = mailbox.mbox(mbox_name)
# mbox = mailbox.mbox('2016-January.txt')
i = 1
data = {}
for message in mbox:
    try:
        dt = parser.parse(message['Date'])
    except ValueError:
        print("Error: Date not readable: " + message['Date'])
    key = str(dt.year) + "-" + str(dt.month)
    if (i % 200 == 0):
        print("Reading mails in " + key)
    data[key] = data.setdefault(key, 0) + 1
    i += 1

# Write CSV file
f = open(mbox_name + "-analysis.csv", 'w')
for (k, v) in sorted(data.items()):
    f.write(str(k) + "," + str(v))
f.close