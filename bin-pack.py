#!/usr/bin/env python

from packer import *

def test_packer(packer_name, packer, items, fill_limit):
    print "Packer: %s" % (packer_name)
    print ""

    (locations, other) = packer.pack(items, fill_limit)

    total_weight = sum(item.weight for item in items)
    avg_weight = float(total_weight) / len(locations)

    def print_location(location):
        tot_weight = 0
        tot_value = 0

        for item in location.items:
            tot_weight += item.weight
            tot_value += item.value

            print "\tWeight: %d, Value: %d" % (item.weight, item.value)
        
        deviation = abs(tot_weight - avg_weight)

        print "Total Weight: %d, Total Value: %d, Deviation: %f" % (tot_weight, tot_value, deviation)
        print ""

        return deviation
    
    tot_deviation = 0
    for location in locations:
        print "Location %d" % (location.name)
        tot_deviation += print_location(location)

    print "Average Deviation: %f" % (tot_deviation / len(locations))
    print ""

    print "Not stored"
    print_location(other)

    print ""

if __name__ == "__main__":
    location_count = 4

    packer1 = Packer1(location_count)
    packer2 = Packer2(location_count)
    
    items1 = [Item(8, 1),
            Item(6, 1),
            Item(6, 1),
            Item(4, 1),
            Item(2, 1)]

    items2 = [Item(2, 1),
            Item(2, 1),
            Item(3, 1),
            Item(4, 1),
            Item(5, 1),
            Item(6, 1),
            Item(8, 1),
            Item(1, 1)]

    items3 = [Item(8, 1),
            Item(8, 1),
            Item(10, 1),
            Item(4, 1),
            Item(6, 1),
            Item(2, 1),
            Item(3, 2),
            Item(2, 1)]

    fill_limit1 = 10
    fill_limit2 = 8

    # Simple test
    test_packer("Packer1", packer1, items1, fill_limit1)
    test_packer("Packer2", packer2, items1, fill_limit1)
    
    # Simple test 2
    test_packer("Packer1", packer1, items2, fill_limit1)
    test_packer("Packer2", packer2, items2, fill_limit1)

    # Oversubscription test
    test_packer("Packer1", packer1, items3, fill_limit1)
    test_packer("Packer2", packer2, items3, fill_limit1)

    # Oversubscription test 2
    test_packer("Packer1", packer1, items3, fill_limit2)
    test_packer("Packer2", packer2, items3, fill_limit2)

