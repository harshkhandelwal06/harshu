wining_number=54
user_input=int(input("enter the number : "))
if wining_number==user_input:
    print("you are wining the game ")
else:
    if user_input < wining_number:
        print("too low !")
    else:
        print("too high ") 