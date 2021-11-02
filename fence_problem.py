# functions go here

def num_check(question):
    valid = False

    print(question)
    
    while not valid:
        response = float(input("Enter a number: "))

        if response > 0:
            valid = True
        else: 
            print("Please enter a number greater than 0.")
        
    return response

#Main program
print()
print("***** area/perimeter calculator *****")
print()

width = num_check("Width: ")
height = num_check("Height: ")

perimeter = 2 * (width + height) 

cost = 10 * perimeter

print("Perimeter: {:.2f} units".format(perimeter))
print("cost: {:.2f} dollars".format(cost))
print()
print()
print("Thank you, you now have your area/perimeter")











