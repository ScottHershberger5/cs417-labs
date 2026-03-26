"""
Lab 15: Heap Basics — Getting comfortable with heapq

Tasks 1 and 2: Explore the heapq API and work with tuple priorities.
"""

import heapq


# ── Task 1: Heap Basics ─────────────────────────────────────────────


def push_and_pop(values):
    """Push all values onto a heap, then pop them all off.

    Args:
        values: A list of numbers.

    Returns:
        A list of the same numbers in ascending order.
    """
    # TODO: Create a heap, push each value, pop them all off
    heap = []
    for val in values:
        heapq.heappush(heap, val)
    list_again = []
    for i in range(len(values)):
        list_again.append(heapq.heappop(heap))
    return list_again


def heapify_and_peek(values):
    """Turn a list into a heap and return the smallest value.

    Args:
        values: A list of numbers.

    Returns:
        The smallest value (without removing it from the heap).
    """
    # TODO: Use heapq.heapify(), then peek with h[0]
    heap = values[:]
    heapq.heapify(heap)
    return heap[0]


def top_k_smallest(values, k):
    """Return the k smallest values in ascending order.

    Args:
        values: A list of numbers.
        k: How many smallest values to return.

    Returns:
        A list of the k smallest values, sorted ascending.
    """
    # TODO: Use heapq to find the k smallest values
    heap = values[:]
    heapq.heapify(heap)
    k_smallest = []
    for i in range(k):
        k_smallest.append(heapq.heappop(heap))
    return k_smallest


# ── Task 2: Tuple Priorities ────────────────────────────────────────


def sort_by_priority(tasks):
    """Sort tasks by priority, maintaining FIFO order for equal priorities.

    Args:
        tasks: A list of (priority, description) tuples.

    Returns:
        A list of description strings in priority order.
        Same-priority tasks appear in their original order.
    """
    # TODO: Use a heap with a sequence counter as tiebreaker
    heap = []
    for k , task in enumerate(tasks): #creating heap with arrival nums
        heapq.heappush(heap, (task[0], k, task[1]))
    
    priority_list = []
    for i in range(len(tasks)):
        priority_list.append(heapq.heappop(heap)[2])
    return priority_list
        
