"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    return max(incoming_list)


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    return min(incoming_list)


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    if incoming_list:
        returnValue = sum(incoming_list)
    else:
        returnValue = 0
    return returnValue


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    currentMaxValue = 0
    maxKey = None
    if incoming_dict:
        for key,value in incoming_dict.items():
            if len(value) > currentMaxValue:
                maxKey = key
                currentMaxValue = len(value)
        returnValue = maxKey
    else:
        returnValue = None
    return returnValue
    
