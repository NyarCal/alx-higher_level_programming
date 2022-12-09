#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    
    # Create a set containing all elements from set_1 that are not in set_2
    
    only_in_set_1 = set_1 - set_2
    
    # Create a set containing all elements from set_2 that are not in set_1
    
    only_in_set_2 = set_2 - set_1
   
    # Return the union of the two sets
    
    return only_in_set_1 | only_in_set_2

