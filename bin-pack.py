#!/usr/bin/env python

from packer import *

def get_packer(bin_count, bin_size):
    return Packer2(bin_count, bin_size)

if __name__ == "__main__":
    bin_count = 4
    bin_size  = 10

    packer = get_packer(bin_count, bin_size)
    
    items = [Item(8, 1),
            Item(6, 1),
            Item(6, 1),
            Item(4, 1),
            Item(2, 1)]

    fill_limit = 10

    (bins, other) = packer.pack(items, fill_limit)

    def print_location(location):
        tot_weight = 0
        tot_value = 0

        for item in location.items:
            tot_weight += item.weight
            tot_value += item.value

            print "\tWeight: %d, Value: %d" % (item.weight, item.value)
        
        print "Total Weight: %d, Total Value: %d" % (tot_weight, tot_value)
        print ""

    for location in bins:
        print "Location %d" % (location.name)
        print_location(location)

    print "Not stored"
    print_location(other)

