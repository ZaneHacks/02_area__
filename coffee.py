print()
print("*** Coffee Order Demo***")

keep_going = ""
while keep_going == "":

    want_coffee = input ("do you want coffee?:").lower()
    if want_coffee != "yes":
        print("wrong answer, you always want coffee")
        continue

    else:
        print("Good answer, you always want coffee")
        break

print()
print("end of program")
print()



