import SortedItem

class SortingMap:

    # Create empty bucket list of given size
    def __init__(self, size, color_tolerance):
        self.color_tolerance = color_tolerance
        self.size = size
        self.index = 0
        self.sort_dict = {}
 
    def putSortedItem(self, item):
        if len(self.sort_dict) < self.size:
            self.sort_dict.update([item.getColor(), item.getShape()], self.index)
            index += 1

    def isMapFull(self):
        return True if len(self.sort_dict) >= self.size else False

    