# check user choice is 'interger', 'text' 'image'
def user_choice():

    # lists of valid responces
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic"]
    
    Valid = False
    while not Valid:

        # ask use for choice and change responce for lowercase
        responce = input("File type (integer / text / image): ").lower()

        # checks for valid responce and returns text, integer or image
       
        if responce in text_ok:
            return "text"

        elif responce in integer_ok:
            return "integer"

        elif responce in image_ok:
            return "image"

        elif responce == "i":
            want_integer = input("press <enter> for an integer or any key for an image: ") 
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            # if responce is not valid, output an error
            print("please choose a vild file type!")
            print()