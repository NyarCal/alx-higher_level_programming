#!/usr/bin/python3
def common_elements(set_1, set_2):
    
    # Create a set to store the common elements
    
    common = set()
    
    # Loop through the elements in set_1
    
    for element in set_1:
        
        # If the element is also in set_2, add it to the common set
        
        if element in set_2:
            
            common.add(element)
            
    # Return the set of common elements
    
    return common

