print("Aloha brah! What's your name?") 

name = input("")

print("What up" + name + "How old are you")

age = input("")

print("Dude, you will be", str(int(age)+1) + "next year!")

if not age.isnumeric():
    print('INPUT ERROR: Please enter a number!')
    quit(1)