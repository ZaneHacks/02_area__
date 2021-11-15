# checks input is a number more than a given value
def num_checker(question, low):
    valid = False
    while not valid:

        error = "please enter an integer that is more than"
        "(or equal to) {}".format(low)

        try:  

            # ask user to enter a number
            responce: