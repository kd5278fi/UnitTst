def is_tens(number):
    """
    Return true if the number is a multiple of 10
    """
    if number % 10 != 0:
        #print ("False")
        return False

    #print ("True")
    return True


def next_tens(number):
    """
    Finds the next highest number by ten
    """
    index = number
    while True:
        index += 1
        if is_tens(index):
            print (index)
            break


