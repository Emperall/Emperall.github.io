print('Do you want to play my quiz? ')
playing = input()
points = 0
if playing != "yes":
    print("Okay, sorry ;c")
    quit()

print("Okay, let's play! ")

answer = input("What does 'CPU' mean? ")
if answer == "Central Processing Unit":
    print("That is correct!")
    points += 1
    print("You have: ",points, "points")

else:
    print("Incorrect..")
    points -= 1
    print("You have: ", points, "points")

answer = input("What does 'GPU' mean? ")
if answer == "Graphics Processing Unit":
    print("That is correct!")
    points += 1
    print("You have: ", points, "points")
else:
    print("Incorrect..")
    points -= 1
    print("You have: ", points, "points")

answer = input("What does 'RAM' mean? ")
if answer == "Random Access Memory":
    print("That is correct!")
    points += 1
    print("You have: ", points, "points")
else:
    print("Incorrect..")
    points -= 1
    print("You have: ", points, "points")

answer = input("What is the Motherboard? ")
if answer == "It is a circuit board":
    print("That is correct!")
    points += 1
    print("You have: ", points, "points")
else:
    print("Incorrect..")
    points -= 1
    print("You have: ", points, "points")

print("Your total points: ", points)
print("Thank you for playing!")


