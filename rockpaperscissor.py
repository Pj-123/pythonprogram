import random
def game(pratik,prakhar):
    if pratik == prakhar:
        return None
    elif pratik == 'R':
        if prakhar == 'P':
            return True
        elif prakhar == 'S':
            return False
    elif pratik == 'P':
        if prakhar == 'R':
            return False
        elif prakhar == 'S':
            return True
    elif pratik == 'S':
        if prakhar == 'R':
            return True
        elif prakhar == 'P':
            return False

prakhar=input("choose something prakhar :rock,paper or scissor ")
number=random.randint(1,3)
if number == 1:
    pratik = 'R'
elif number == 2:
    pratik = 'P'
elif number == 3:
    pratik = 'S'
z=game(pratik,prakhar)
print("pratik choose",str(pratik))
print("prakhar choose",str(prakhar))
if z == None:
    print("match draw")
elif z:
    print("prakhar won")
else:
    print("pratik won")




