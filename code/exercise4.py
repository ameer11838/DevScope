# WRITE YOUR CODE HERE

def is_nested(my_dict):
    for value in my_dict.values():
        if type(value) == list or type(value) == tuple or type(value) == dict:
            return True
    return False


# test code below