Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
                                                                           
class RandomizedSet:

    def __init__(self):
        self.mp = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return 0
        self.arr.append(val)
        self.mp[val] = len(self.arr)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return 0
        i = self.mp[val]
        self.mp[self.arr[-1]] = i
        self.arr[i] = self.arr[-1]
        self.mp.pop(val)
        self.arr.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
