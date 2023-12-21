class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        res = 0
        for char in key:
            res += ord(char)
        return res % self.size

    def insert(self, value):
        key = self._hash_function(value)
        bucket = self.table[key]
        for i, existing_value in enumerate(bucket):
            if existing_value == value:
                return key, i
        bucket.append( value )
        return key, len(bucket) - 1

    def search(self, value):
        key = self._hash_function(value)
        bucket = self.table[key]
        for i, stored_value in enumerate(bucket):
            if stored_value == value:
                return key, i  
        raise KeyError(f"Key '{key}' not found in the hashtable.")

    def remove(self, value):
        key = self._hash_function(value)
        bucket = self.table[key]
        for i, (stored_value, _) in enumerate(bucket):
            if stored_value == value:
                del bucket[i]  # Remove key-value pair from the bucket
                return
        raise KeyError(f"Key '{key}' not found in the hashtable.")
