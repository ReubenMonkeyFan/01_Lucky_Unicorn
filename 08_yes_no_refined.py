show_instructions = ""
while show_instructions.lower() != "xxx":

# ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()


    #if they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("Program continues")

    elif show_instructions == "no" or show_instructions == "n":
        print("Print instructions")

    # if they say no output 'display instructions'
    else:
        print("Please answer Yes / No")
