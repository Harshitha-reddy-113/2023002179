# Notification Priority Inbox System

## Priority Logic

Notifications are prioritized using both type and recency.

Priority Order:

1. Placement
2. Result
3. Event

Weights:

* Placement = 3
* Result = 2
* Event = 1

## Approach

1. Read notifications.
2. Assign a weight based on notification type.
3. Convert timestamp into a comparable value.
4. Generate a priority score.
5. Maintain the Top 10 notifications using a Min Heap.
6. Display notifications sorted by highest priority.

## Data Structure Used

Min Heap (Priority Queue)

### Why Heap?

A heap efficiently maintains only the highest-priority notifications.

When new notifications arrive:

* Calculate priority score.
* Compare with minimum element.
* Replace if higher priority.

This avoids sorting the entire dataset repeatedly.

## Complexity Analysis

Time Complexity:

* Building Heap: O(n log 10)
* Retrieval: O(10 log 10)

Overall: O(n)

Space Complexity:

O(10)

## Future Improvements

* Live API integration
* Read/Unread tracking
* User-specific notification preferences
* Real-time notification updates
