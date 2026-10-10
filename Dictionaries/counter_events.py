from collections import Counter

events = ["failed", "success", "failed", "failed", "success"]
for event, count in Counter(events).items():
    print(f"{event}: {count}")
