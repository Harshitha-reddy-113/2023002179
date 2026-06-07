import json
import heapq
from datetime import datetime

weights = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}

with open("notifications.json", "r") as file:
    data = json.load(file)

notifications = data["notifications"]

heap = []

for notification in notifications:

    notif_type = notification["Type"]

    dt = datetime.strptime(
        notification["Timestamp"],
        "%Y-%m-%d %H:%M:%S"
    )

    score = (
        weights[notif_type] * 10000000000
        + dt.timestamp()
    )

    item = (score, notification)

    if len(heap) < 10:
        heapq.heappush(heap, item)
    else:
        if score > heap[0][0]:
            heapq.heapreplace(heap, item)

top_notifications = sorted(
    heap,
    key=lambda x: x[0],
    reverse=True
)

print("\nTOP 10 PRIORITY NOTIFICATIONS\n")

for i, (_, notif) in enumerate(top_notifications, start=1):
    print(f"{i}. {notif['Type']}")
    print(f"   Message   : {notif['Message']}")
    print(f"   Timestamp : {notif['Timestamp']}")
    print()