class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Simple hash function
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        # Always append the new value
        bucket.append((key, value))
            
    def get(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for item in bucket:
            if isinstance(item, dict) and item.get('district') == key:
                return item
        return None
    
    def keys(self):
        all_keys = set()
        for bucket in self.table:
            for item in bucket:
                # Assuming each 'item' is a dictionary and 'district' is the key
                all_keys.add(item['district'])
        return list(all_keys)