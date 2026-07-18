# WRITE YOUR CODE HERE
import json

def compare(file1, file2):
    with open(file1) as f1:
        dict1 = json.load(f1)

    with open(file2) as f2:
        dict2 = json.load(f2)

    if dict1 == dict2:
        return "The dictionaries are equal"
    elif len(dict1) > len(dict2):
        return "Dictionary 1 has more items than dictionary 2"
    elif len(dict2) > len(dict1):
        return "Dictionary 2 has more items than dictionary 1"
    else:
        return "Dictionary 1 and Dictionary 2 have the same number of items"

# test code below
if __name__ == "__main__":
    import sys

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    print(compare(file1, file2))