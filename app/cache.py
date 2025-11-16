import time

class Cache:
    def __init__(self):
        self.data = {}
        self.expire_time = 10  # seconds

    def set(self, key, value):
        self.data[key] = {
            "value": value,
            "timestamp": time.time()
        }

    def get(self, key):
        if key not in self.data:
            return None

        item = self.data[key]
        if time.time() - item["timestamp"] > self.expire_time:
            return None

        return item["value"]
