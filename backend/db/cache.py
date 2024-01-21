class MyCache:
    cache = {}

    @staticmethod
    def get(key):
        if key not in MyCache.cache:
            return None
        return MyCache.cache[key]

    @staticmethod
    def set(key, value):
        MyCache.cache[key] = value
