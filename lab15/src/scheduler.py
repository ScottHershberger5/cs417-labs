"""
Lab 15: Task Scheduler — A priority queue in action

Task 3: Build a TaskScheduler class using heapq.
"""

import heapq


class TaskScheduler:
    """A priority-based task scheduler.

    Tasks are added with a priority (lower number = more urgent).
    Tasks with the same priority are processed in FIFO order.
    """

    def __init__(self):
        """Initialize the scheduler."""
        heap = []
        # heapq.heapify(heap)
        self.schedule = heap
        self.len = 0

    def add_task(self, priority, description):
        """Add a task to the scheduler.

        Args:
            priority: An integer priority (lower = more urgent).
            description: A string describing the task.
        """
        # TODO: Push onto the heap with a tiebreaker
        self.len += 1
        heapq.heappush(self.schedule, (priority, self.len, description))

    def next_task(self):
        """Remove and return the highest-priority task's description.

        Returns:
            The description string, or None if empty.
        """
        # TODO: Pop from the heap, return the description
        if self.len == 0:
            return None
        
        self.len -= 1
        return heapq.heappop(self.schedule)[2]


    def peek(self):
        """Return the highest-priority task's description without removing it.

        Returns:
            The description string, or None if empty.
        """
        # TODO: Look at h[0] without popping
        if self.len:
            return self.schedule[0][2]
        return None

    def __len__(self):
        """Return the number of pending tasks."""
        # TODO: Return the length of the heap
        return self.len

    def is_empty(self):
        """Return True if there are no pending tasks."""
        # TODO
        if self.len:
            return False
        return True
