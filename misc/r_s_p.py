''' rock, scissors, paper'''
def haf():
    ''' main '''
    score = [0, 0]
    stat = []
    while True:
        inpt = read_input()
        #print("Your choice: " + inpt)
        if inpt == "quit":
            print("By")
            input()
            break
        elif inpt == "statistic":
            pass
        else:
            rsp = generate_response()
            stat.append((inpt, rsp))
            #inner brackets make a tupple , as append expects just one argument
            print("Your choice: " + inpt + "    My choice: " + rsp)
            if evaluation(inpt, rsp) == "user":
                score[0] += 2
                print("You have won    " + str_score(score))
            elif evaluation(inpt, rsp) == "syst":
                score[1] += 2
                print("I have won     " + str_score(score))
            else:
                score[0] += 1
                score[1] += 1
                print("Draw            " + str_score(score))

def read_input():
    '''user's input'''
    valid_input = ["rock", "scissors", "paper", "r", "p", "s", "quit", "q",
                   "display_statistic", "d"]
    while True:
        inpt = input('Choice: ').lower()
        if inpt in valid_input:
            if inpt in ["rock", "r"]:
                return 'rock'
            elif inpt in ["scissor", "s"]:
                return 'scissors'
            elif inpt in ["paper", "p"]:
                return 'paper'
            elif inpt in ["display_statistic", "d"]:
                return 'statistic'
            else:
                return 'quit'

        print("Invalid input. Valid input: " + ', '.join(valid_input))

def generate_response():
    '''generate system respones'''
    import random
    return random.choice(["rock", "scissors", "paper"])

def evaluation(user, syst):
    '''find the winner'''
    if user == syst:
        return "draw"
    win = {"rock":"scissors", "scissors": "paper", "paper": "rock"}
    if win[user] == syst:
        return "user" # user wins
    else:
        return "syst" #system wins


def str_score(score):
    '''create string for score'''
    return "Score: " + str(score[0]) + ":" + str(score[1])
def display_statistic():
    '''display statistic'''
    print("Statistic:")
haf()
