def swap(dictionary):
    swapped = {}

    for key in dictionary:
        value = dictionary[key]

        try:
            swapped[value] = key
        except TypeError:
            return "Cannot swap the keys and values for this dictionary"

    return swapped