# function goes here
def yes_no (question):
    valid = False
    while not valid:
        response = input(question).strip().lower()

        if response == "y" or response == "yes":
            response = "yes"
            return response


        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes or no")



# main function

show_instructions = yes_no("Have you played before?")

print("You chose {}".format(show_instructions))
print()
having_fun = yes_no("Are you having fun?")
print("You said {} to having fun".format(having_fun))
