#ask the user if they have played before
show_instructions = input("Have you played this game before? ").lower()


#if they say yes, output 'program continues'
if show_instructions =="yes" or show_instructions =="y":
    print("program continues")

#If they say no, ouput 'display instructions'
elif show_instructions =="no" or show_instructions =="n":
    print("Display instructions")

#If they say anything else, ouput 'please answer Yes / No'
else:
    print("Please answer Yes / No")
