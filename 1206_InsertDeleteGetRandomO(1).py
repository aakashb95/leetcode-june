class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []  # a list to store incoming values
        self.pos = {}  # to store position of incoming values

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.vals.append(val)
            self.pos[val] = len(self.vals) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            idx = self.pos[val]
            last = self.vals[-1]
            self.vals[idx] = last
            self.pos[last] = idx
            self.vals.pop()
            del self.pos[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
