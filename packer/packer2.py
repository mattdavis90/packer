from operator import attrgetter

from bin import Bin

class Packer(object):
    def __init__(self, bin_count, bin_size):
        self._bin_count = bin_count
        self._bin_size = bin_size

    def pack(self, items, fill_limit):
        bins = []
        other = Bin(-1)

        for x in range(0, self._bin_count):
            bins.append(Bin(x))

        items = sorted(items, key=attrgetter('weight'), reverse=True)
        
        for item in items:
            # Search through the bins looking for space starting at the bin that was touched longest ago
            bins.append(bins.pop(0)) # Moves the touched bin to the end of the list
        
        return (bins, other)

