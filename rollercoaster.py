bill = 0
height = float(input("What is your height in meters? "))
if (height>1.20):
    age = int(input("You can ride\nbut tell me, what is your age? "))
    if (age < 12):
        bill += 5
    elif (age >= 12 and age <= 18):
        bill += 7
    elif (age > 18):
        bill += 12
    wantPhotos = input("Do you want photos? Y/N ")
    if (wantPhotos.upper() == "Y"):
        bill += 3
    print("The total bill is: $"+str(bill))
else:
    print("You can't ride.")

