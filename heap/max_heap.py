class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if len(self.storage) > 0:
            ret_val = self.storage[0]
            temp = self.storage[-1]
            if len(self.storage) > 1:
                self.storage[0] = temp
                self.storage.pop()
                self._sift_down(0)
            else:
                return self.storage.pop()
            return ret_val

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return
        if self.storage[index] > self.storage[(index - 1) // 2]:
            temp = self.storage[(index - 1) // 2]
            self.storage[(index - 1) // 2] = self.storage[index]
            self.storage[index] = temp
        else:
            return
        self._bubble_up((index - 1) // 2)

    def _sift_down(self, index):
        left = None
        right = None
        if len(self.storage) > 2*index + 1:
            left = self.storage[2*index + 1]
        if len(self.storage) > 2*index + 2:
            right = self.storage[2*index + 2]

        ind = None
        if left is not None and right is not None:
            if left > right:
                ind = 2 * index + 1
            else:
                ind = 2 * index + 2
        elif left is not None:
            ind = 2* index + 1
        elif right is not None:
            ind = 2 * index + 2
        else:
            return
        # print(ind)
        temp = self.storage[ind]
        self.storage[ind] = self.storage[index]
        self.storage[index] = temp
        self._sift_down(ind)

