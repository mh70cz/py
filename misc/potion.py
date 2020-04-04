def menu():
    '''Print menu and select'''
    while True:
        vaild_input = ["1", "1.", "2", "2.", "3", "3.", "q", "Q"]
        print("1. Invisibility")
        print("2. Antidote")
        print("3. Aging")
        print("q  Quit")
        choice = input("Choose your potion:")
        if choice in vaild_input:
            if choice in ["1", "1."]:
                return "1"
            elif choice in ["2", "2."]:
                return "2"
            elif choice in ["3", "3."]:
                return "3"
            else:
                return "q"
        else:
            print("Invalid input")
            print("Valid input is: 1,  2,  3,  q")

while True:
    ch = menu()
    print("Your choice: " + ch)
    if ch == "q":
        break
    

