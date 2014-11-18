from operator import attrgetter

from bin import Bin

class Packer(object):
    def __init__(self, bin_count, bin_size):
        self._bin_count = bin_count
        self._bin_size = bin_size

    def pack(self, items, fill_limit):
        bins = []
        other = Bin()

        for x in range(0, self._bin_count):
            bins.append(Bin())

        items = sorted(items, key=attrgetter('value'))
        
        for item in items:
            stored = False

            for location in bins:
                if location.weight < fill_limit and item.weight <= (fill_limit - location.weight):
                    location.add_item(item)
                    stored = True

                    break

            if not stored:
                other.add_item(item)

        return (bins, other)

