#!/usr/bin/python3
def search_replace(my_list, search, replace):
    
    # Create a new list with the same size as the initial list
    
    new_list = [None] * len(my_list)
    
    # Iterate over the initial list
    
    for i in range(len(my_list)):
        
        # Check if the current element is the one to replace
        
        if my_list[i] == search:
            
            # If it is, replace it with the new element
            
            new_list[i] = replace
            
        else:
            
            # If it is not, keep the original element
            
            new_list[i] = my_list[i]
            
    # Return the new list
    
    return new_list

