# funtions go here

# puts a series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # make string with five characters
    end = decoration * 5

    # add decoration to the start and end of the statement
    statement = "{} {} {}".format(ends, text, ends,)

    print()   
    print(statement)
    print()

    return ""

# main routene goes here
statement_generator("bit calculator for Integers, text and images","-")


# display instructions if user has not used the program before

# loop to allow multiple calculations per sesions
keep_going = ""
while keep_going =="":

    # ask the user for the file type 
    data_type = user_choice()
    print("you chose", data_type)

    # for intergers, ask for interger 
    if data_type =="interger":
        var_interger = num_check("enter an interge:", 0)

    # (must be an interger more than / eqaul to 0)
    elif data_type == num_check("image"):
         image_width = num_check(image_width)
    # for images, ask for witdh and height
