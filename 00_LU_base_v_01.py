

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

def instructions():
    print("**** How To Play ****")
    print()
    print("The rules of the game go here")
    print()
    return""

def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            #ask the question
            response = int(input(question))

            # If the amount is too low / high give
            if low < response <= high:
                    return response


        # output an error
            else:
                print(error)

        except ValueError:
            print(error)

# main routine

played_before = yes_no("Have you played before? ")

if played_before == "no":
    instructions()

print("Program Continues")

# Ask user how much they want to play with
how_much = num_check("How much would you like to play with? ", 0, 10)
print()
print("You will be spending ${}".format(how_much))
