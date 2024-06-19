from random import randint

choice0 = "fold"
choice1 = "unfold"
ran = randint(0,1)
dan = randint(0,1)

user = input("Choose Fold or Unfold >")
if user.capitalize() == "Fold":
    p1 = "Fold"
    print("Player 1 = ", user)
else:
    p1 = "Unfold"
    print("Player 1 = Unfold")

com1 = ran
if com1 == 1:
    com1 = "Fold"
    print("Computer 1 = Fold")
else:
    com1 = "Unfold"
    print("Computer 1 = Unfold")

com2 = dan
if com2 == 1:
    com2 = "Fold"
    print("Computer 2 = Fold")
else:
    com2 = "Unfold"
    print("Computer 2 = Unfold")


if (p1 == "Fold" and com1 == "Unfold" and com2 == "Unfold") or (p1 == "Unfold" and com1 == "Fold" and com2 == "Fold"):
    print("Player 1 Win!!!!")


elif (p1 == "Unfold" and com1 == "Fold" and com2 == "Unfold") or (p1 == "Fold" and com1 == "Unfold" and com2 == "Fold"):
    print("Computer 1 Win!!!!")


elif (p1 == "Unfold" and com1 == "Unfold" and com2 == "Fold") or (p1 == "Fold" and com1 == "Fold" and com2 == "Unfold"):
    print("Computer 2 Win!!!!")


else:
    print("No one wins!!!")


