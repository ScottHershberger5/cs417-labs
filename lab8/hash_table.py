"""
Lab 8: Build Your Own Hash Table

In this lab you will implement a hash table from scratch using
separate chaining (each bucket is a list of [key, value] pairs).

Complete the four methods marked with TODO.
Do NOT change the method signatures or the __init__ method.

Run tests:
    pytest -v
"""


class HashTable:
    """A hash table using separate chaining for collision resolution."""

    def __init__(self, size=10):
        """Create an empty hash table with the given number of buckets."""
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    # ── TODO 1: Hash Function ─────────────────────────────────────

    def _hash(self, key):
        """
        Return a bucket index for the given key.

        Use Python's built-in hash() function and modulo (%) to map
        the key to a valid index in range [0, self.size).

        Args:
            key: The key to hash (any hashable type).

        Returns:
            int: A bucket index between 0 and self.size - 1.
        """
        return int(hash(key) % self.size)

    # ── TODO 2: Put ───────────────────────────────────────────────

    def put(self, key, value):
        """
        Insert or update a key-value pair.

        Steps:
            1. Compute the bucket index using _hash().
            2. Check if the key already exists in that bucket.
               - If it does, UPDATE the value in place.
               - If it doesn't, APPEND a new [key, value] pair.
            3. Update self.count if a new key was added.

        Args:
            key:   The key to insert.
            value: The value to associate with the key.
        """
        bucket = self._hash(key)
        if self.table[bucket]:
            for list in self.table[bucket]:# may have to do bucket -1
                if list[0] == key:
                    list[1] = value
                else:
                    self.table[bucket].append([key,value])
                    self.count += 1
                    return
        else:
            self.table[bucket].append([key,value])
            self.count += 1

             



    # ── TODO 3: Get ───────────────────────────────────────────────

    def get(self, key):
        """
        Look up a value by key.

        Steps:
            1. Compute the bucket index using _hash().
            2. Search the bucket for a pair with a matching key.
            3. Return the value if found, raise KeyError if not.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key.

        Raises:
            KeyError: If the key is not found.
        """
        bucket = self._hash(key)
        
        for list in self.table[bucket]:
            if list[0] == key:
                return list[1]
        raise KeyError(f"{key} not in hash table.")

    # ── TODO 4: Delete ────────────────────────────────────────────

    def delete(self, key):
        """
        Remove a key-value pair from the table.

        Steps:
            1. Compute the bucket index using _hash().
            2. Search the bucket for a pair with a matching key.
            3. If found, remove it and decrement self.count.
            4. If not found, raise KeyError.

        Args:
            key: The key to remove.

        Raises:
            KeyError: If the key is not found.
        """
        bucket_num = self._hash(key)
        bucket = self.table[bucket_num]
        for index, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[index]
                self.count -= 1
                return
        raise KeyError(f"{key} not in hash table.")

    # ── Provided Methods (do not modify) ──────────────────────────

    def __len__(self):
        """Return the number of key-value pairs in the table."""
        return self.count

    def __contains__(self, key):
        """Support 'in' operator: key in table."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def load_factor(self):
        """Return the current load factor (items / buckets)."""
        return self.count / self.size

    def __repr__(self):
        """Show a readable view of the hash table's internal structure."""
        lines = []
        for i, bucket in enumerate(self.table):
            if bucket:
                pairs = ", ".join(f"{k!r}: {v!r}" for k, v in bucket)
                lines.append(f"  [{i}] {pairs}")
            else:
                lines.append(f"  [{i}] empty")
        return f"HashTable({self.count} items, {self.size} buckets):\n" + "\n".join(lines)
