class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Simple hash function
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self._hash(key)
        key_exists = False
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def get(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if key == k:
                return v
        return None

    def keys(self):
        all_keys = []
        for bucket in self.table:
            for key, _ in bucket:
                all_keys.append(key)
        return all_keys