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
        
        # Search through the bins looking for space starting at the bin that was touched longest ago
        for item in items:
            stored = False

            for idx, location in enumerate(bins):
                if location.weight < fill_limit and item.weight <= (fill_limit - location.weight):
                    location.add_item(item)
                    bins.append(bins.pop(idx)) # Moves the touched bin to the end of the list
                    stored = True

                    break

            if not stored:
                other.add_item(item)
        
        return (bins, other)

