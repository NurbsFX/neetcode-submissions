class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.store:
            self.store[timestamp] = {}
        self.store[timestamp][key] = value

    def get(self, key: str, timestamp: int) -> str:
        n = 0
        mostRecentTimestamp = -1
        for timestamp_prev in self.store:
            n += 1
            if timestamp_prev <= timestamp and timestamp_prev > mostRecentTimestamp and key in self.store[timestamp_prev]:
                mostRecentTimestamp = timestamp_prev
        if mostRecentTimestamp == -1:
            return ""
        return self.store[mostRecentTimestamp][key]
