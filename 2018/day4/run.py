import sys
import datetime

def transition(curr_id, cmd):
    if cmd.startswith("Guard"):
        return cmd.split(" ")[1].split("#")[1], False
    if cmd.startswith("wakes up"):
        return curr_id, True
    return int(curr_id), False

def update(d, prev_date, date, curr_id):
    if curr_id not in d:
        d[curr_id] = {}
    curr = prev_date
    while curr < date:
        min = curr.minute
        if min not in d[curr_id]:
            d[curr_id][min] = 1
        else:
            d[curr_id][min] += 1
        curr = curr + datetime.timedelta(minutes = 1)
    return (date - prev_date).seconds / 60

id_min_count = {}
id_durations = {}

curr_id = -1
awoke = True
prev_date = None
for line in sys.stdin:
    parts = line.split("] ")
    date = datetime.datetime.strptime(parts[0].split("[")[1], "%Y-%m-%d %H:%M")
    cmd = parts[1]
    curr_id, awoke = transition(curr_id, cmd)
    if awoke:
        duration = update(id_min_count, prev_date, date, curr_id)
        if curr_id not in id_durations:
            id_durations[curr_id] = duration
        else:
            id_durations[curr_id] += duration
    prev_date = date

max_id = None
max_duration = -1
for id, duration in id_durations.items():
    if duration > max_duration:
        max_id = id
        max_duration = duration

max_min = None
max_count = -1
for min, count in id_min_count[max_id].items():
    if count > max_count:
        max_count = count
        max_min = min

print(id_min_count)
print(id_durations)
print(max_id)
print(max_duration)
print(max_min)
print(max_count)
print(max_min * max_id)

for id, min_count in id_min_count.items():
    for min, count in id_min_count[id].items():
        if count > max_count:
            max_count = count
            max_min = min
            max_id = id
print(max_count)
print(max_id)
print(max_min* max_id)
