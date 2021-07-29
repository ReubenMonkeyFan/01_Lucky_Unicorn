

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
# main function

played_before = yes_no("Have you played before?")

if played_before == "no":
    instructions()

print("Program Continues")
