import random 

def game(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True 
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False
       

print("Computer Turn: Rock(r) Paper(p) Scissor(s) ?" )
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'


you = input("Your's Turn: Rock(r) Paper(p) Scissor(s) ?" )
a = game(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("The game is tie !")
elif a == True:
    print("You Win !")
else:
    print("You Loose !")
