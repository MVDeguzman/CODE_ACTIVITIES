import imp


import os

isContinue = True
no=0
while isContinue == True:
    ask = input("whould you like to add another triangle (yes / no) -->")
    if ask.lower() == "no":
        print("PROGRAM TERMINATED")
        break
        isContinue = False
    else:
        os.system('cls')
        no +=1

