print("THIS PROGRAM IS FOR FINAL PROJECT OF VINCENT FROM BSIT-1A")
print("TO ENTER TO THE PROGRAM PLEASE ENTER THE PASSWORD")
paword= input("ENTER THE PASSWORD:")
if paword.lower== "password":
    print("YOU HAVE ACCESS IN THE PROGRAM")
else:
      print("THE PROGRAM IS TERMINATED")


def act22():
      
      def act1():
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\b\t*\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b* * *",
            "\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b\b\b* * * * *\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b\b\b\b\b* * * * * * *",
            "\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b\b\b* * * * *\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b* * *",
            "\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t*\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b")

      def act2():
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))

            print(num1, "\nFloor Divided to", num2 ,"=", num1 // num2)

      def act3():
            fullname = input("please input your full name:")

            City = input("please input your city:")

            Province = input("please input your province:")

            Postal_code = input("please input the postal code of the province:")

            Cellphonenumber = input("please input your cellphone number:")

            Email = input("please input your email:")

            Birthday = input("please input you birhday:")

            BirthPlace = input("please input your birth place:")

            Age = input("please input your age:")

            CivilStatus = input("please input your civil status:")

            Height = input("please input your height in ft:")

            Weight = input("please input your weight in kg:")

            Religion = input("please input your religion:")

            Gender = input("please input your gender:")

            Citezenship = input("please input your cintezenship:")

            FatherName = input("please input your father's name:")

            SiblingName = input("please input your sibling's name:")

            print("My name is:" + fullname + 
                "\nI'm from the city of:" + City + 
                "\nI'm from the province of:" + Province + 
                "\nThe postal code of:" + Province + ",is the:" + Postal_code + 
                "\nMy cellphone number is:" + Cellphonenumber + 
                "\nMy Email is:" + Email + 
                "\nMy Birthday is:" + Birthday + 
                "\nMy Birth Place:" + BirthPlace + 
                "\nMy age is:" + Age + 
                "\nMy civil status is:" + CivilStatus +
                "\nMy height in Ft is:" + Height + 
                "\nMy weight in kilogram is:" + Weight + 
                "\nMy religion is:" + Religion + 
                "\nMy gender:" +Gender + 
                "\nMy citezenship is" + Citezenship + 
                "\nMy Father's full name is:" + FatherName + 
                "\nMy sibling's full name is:" + SiblingName + 
                "\nThis is my BIONOTE") 

      def act4():
            number1 = eval(input("\n\n\t\t\bEnter A Number: "))
            number2 = eval(input("\t\t\bEnter Another Number: "))

            add = number1 + number2
            sub = number1 - number2
            mul = number1 * number2
            div = number1 / number2
            flr_div = number1 // number2
            exp = number1 ** number2
            mod = number1 % number2


            print("\n\n\t\t\t\tThe sum of",number1,"and",number2,"in addition is",add,
            "\n\t\t\t\tThe sum of",number1,"and",number2,"in subtraction is",sub,"\n\t\t\t\tThe sum of",number1,
            "and",number2,"in multiplication is",mul,"\n\t\t\t\tThe sum of",number1,"and",number2,"in division is",div,
            "\n\t\t\t\tThe sum of",number1,"and",number2,"in floor division is",flr_div,"\n\t\t\t\tThe sum of",number1,"and",number2,
            "in exponentiation is",exp,"\n\t\t\t\tThe sum of",number1,"and",number2,"in modulus is",mod,"\n\n ")

      def act5():
            temp = float(input("Enter Temperature in Farenheit: "))

            cel = (temp - 32) * 5/9

            print(f"The conversion of {temp} degrees Farenheit is {round(cel, 2)} degrees Celcius.")

      def act6():
            x = 5
            print(x)

            x += 10
            print(x)

            x += 15
            print(x)

            x+= 10
            print(x)

      def act7():
            gold = 0
            min = input("Hi, What is your name: ")

            isgold = input("Is the mineral Gold? [Yes / No]: ").upper().strip()

            if isgold == "YES":
                  gold += 1
                  print(f"Hi {min}, Your total number of Gold is: {gold}")

            elif isgold == "NO":
                  print("Please input a Gold")

            else:
                  print("Wrong Input")

      def act8():
            pre = int(input("\n\n\tPrelim Score: "))
            mid = int(input("\n\tMidterm Score: "))
            semi = int(input("\n\tSemi-Final Score: "))
            final = int(input("\n\tFinal Score: "))
            quiz = int(input("\n\tQuiz Score: "))
            proj = int(input("\n\tProject Score: " ))

            fg = (pre * 0.15) + (mid * 0.15) + (semi * 0.15) + (final * 0.15) + (quiz * 0.25) + (proj * 0.15)


            print(f"\n\n\tYour grade is {fg}")

            if pre > 100:
                  print("\n\tError. Wrong input")
            elif fg >= 65:
                  print("\n\tCongratulations! You have passed the course")
            else:
                  print("\n\tUnfortunately You Have Failed")

      def act9():
            age = int(input("Enter your Age: "))

            if age > 130:
                  print("Enter your Real Age")
            elif age >= 60 and age <= 130:
                  print("You are a senior")
            elif age >= 46 and age <= 59:
                  print("You are at Post Adulthood")
            elif age >= 32 and age <= 45:
                  print("You are at Mid Adulthood")
            elif age >= 19 and age <= 31:
                  print("You are at an Early Adulthood")
            elif age >= 14 and age <= 18:
                  print("You are a Teenager")
            elif age >= 8 and age <= 13:
                  print("You are at Pre-Teen")
            elif age >= 1 and age <= 7:
                  print("You are a Todler")
            else:
                  print("Enter a your Real Age")

      def act10():
            name= input("Enter your name here:  ")
            isStud = input ("Are you currently enrolled in DLL? [Yes or No]:  ").upper().strip()


            if isStud == "YES":
                  yearLev =input("What year are you currently enrolled? \nF- Freshmen \nS-Sophomore"
                              "\nJ-Junior  \nR-Senior: \nPlease enter your answer here: ").upper().strip()
                  
                  if yearLev == "F":
                        print(f"Hello Freshie {name}, and Welcome to DLL") 
                  elif yearLev == "S":
                        print(f"Hello Sophomore {name}, and Welcome to DLL") 
                  elif yearLev == "J":
                        print(f"Hello Junior {name}, and Welcome to DLL, konti na lang") 
                  elif yearLev == "R":
                        print(f"Hello Senior {name}, Welcome to DLL and congrats pwede kanang humimlay")

            elif isStud == "NO":
                  print("Thank you, Next")

            else:
                  print("Wrong Input")

      def act11():
            for i in range(1, 11):
                  print("Hello World!")
                  print("Happy Foundation")
                  
                  single = False

                  print(f"{single}, That I'm Single")

      def act12():
            for i in range(10, 1, -1):
                  print(i)

      def act13():
            sum = 0

            for i in range(4, 0, -1):
                  i *= i
                  sum += i


            print(i)
            print(sum)

      def act14():
            for i in range(0,11):
                  print(i, end="")
                  for k in range(0,11):
                        print("*", end= (""))
                  print()

      def act15():
            for i in range(0, 11):
                  print(i, end=" ")
                  for k in range(0, i):
                        print("*", end= (" "))
                  print()

      def act16():
            for x in range(1, 11):
                  for z in range(1, x + 1):
                        print(" ", end=" ")
                  for y in range(11, x, -1):
                        print("*", end= " ")

                  print()

      def act17():
            for x in range(6, 0, -1):
                  for y in range(1, x + 1):
                        print(" ", end= " ")

                  for z in range(6, x, -1):
                        print("*", end= " ")

                  for a in range(5, x, -1):
                        print("*", end= " ")

                  print()

            for x in range(1, 6):
                  for y in range(1, x + 2):
                        print(" ", end= " ")

                  for z in range(5, x, -1):
                        print("*", end= " ")

                  for a in range(4, x, -1):
                        print("*", end= " ")

                  print()

      def act18():
            num = int(input("Enter a number of right triangle: ")) 

            for i in range(1, 6):
                  for r in range(1, num + 1):
                        print(" ", end= " ")
                        for j in range(1, i + 1):
                              print("*", end= " ")
                        for k in range(5, i, -1):
                              print(" ", end= " ") 

                  print()

      def act19():
            contin = True
            count = 0

            while contin == True:
                  name = input("Enter a name: ").upper().strip()

                  if name == "STOP":
                        print("The loop has now stopped")
                        print(f"You have entered {count} number of names")
                        break

                  else:
                        count += 1
                        continue

      def act20():
            isContinue = True
            no = 0
            while isContinue == True:
                  ask = input("Would you like to add another triangle [Yes / No]: ").strip().upper()

                  if ask == "no":
                        print("PROGRAM TERMINATED")
                        break
                        isContinue = False

                  else:
                        no += 1
                        for x in range(1,5):
                              for r in range(1,no + 1):
                                    for y in range(1,x + 1):
                                          print(" ", end= " ")
                              
                                    for z in range(1, x, -1):
                                          print("*", end= " ")
                                    print()    
                        continue

      def act21():

            def Hallo(name):
                  print(f"Hello {name}")

            def act2():
                  num1 = int(input("Please enter a number:  "))
                  num2 = int(input("Please enter another number:  "))
                  answer = num1 + num2
                  print(f"The sun of {num1} and {num2} is: {answer}")

            while True:
                  ask = input("Please provide a name: ").upper().strip()
                  if ask =="STOP":
                        Hallo(ask)

      def act23():

            def add(num1, num2):
                  """This function adds the first number and second number returnig sum value"""
                  return print(f"The sum of the numbers are: {num1 + num2}")    

            add()

      def act24():
            
            from Activity23 import add
            import Activity1

            add(21,21)
            Activity1

      def act25():

            def list():

                  courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

                  courses.remove("Delete w/o index")
                  courses.pop()
                  courses.append("DHRS")
                  courses.insert(0, "ABELS")

                  print(courses)

            list()


      try:
            compile = True

            while compile:

                  print("\n\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
                        "\n\tActivity 1 - [1]", "\tActivity 9 - [9]", "\tActivity 17 - [17]"
                        "\n\tActivity 2 - [2]", "\tActivity 10 - [10]", "\tActivity 18 - [18]"
                        "\n\tActivity 3 - [3]", "\tActivity 11 - [11]", "\tActivity 20 - [20]"
                        "\n\tActivity 4 - [4]", "\tActivity 12 - [12]", "\tActivity 21 - [21]"
                        "\n\tActivity 5 - [5]", "\tActivity 13 - [13]", "\tActivity 23 - [23]"
                        "\n\tActivity 6 - [6]", "\tActivity 14 - [14]", "\tActivity 24 - [24]"
                        "\n\tActivity 7 - [7]", "\tActivity 15 - [15]", "\tActivity 25 - [25]"
                        "\n\tActivity 8 - [8]", "\tActivity 16 - [16]", "\tExit - [0]")

                  num = int(input("\n\n\tSelect a Program: "))

                  if num == 1:
                        act1()
                        continue

                  elif num == 2:
                        act2()
                        continue

                  elif num == 3:
                        act3()
                        continue

                  elif num == 4:
                        act4()
                        continue

                  elif num == 5:
                        act5()
                        continue

                  elif num == 6:
                        act6()
                        continue
                  
                  elif num == 7:
                        act7()
                        continue

                  elif num == 8:
                        act8()
                        continue

                  elif num == 9:
                        act9()
                        continue

                  elif num == 10:
                        act10()
                        continue

                  elif num == 11:
                        act11()
                        continue

                  elif num == 12:
                        act12()
                        continue

                  elif num == 13:
                        act13()
                        continue

                  elif num == 14:
                        act14()
                        continue
                        
                  elif num == 15:
                        act15()
                        continue

                  elif num == 16:
                        act16()
                        continue

                  elif num == 17:
                        act17()
                        continue
                  
                  elif num == 18:
                        act18()
                        continue

                  elif num == 19:
                        act19()
                        continue

                  elif num == 20:
                        act20()
                        continue

                  elif num == 21:
                        act21()
                        continue

                  elif num == 23:
                        act23()
                        continue

                  elif num == 24:
                        act24()
                        continue

                  elif num == 25:
                        act25()
                        continue
                  
                  elif num == 0:
                        cont = input("Do you want to continue? [Yes] / [No]: ").upper().strip()

                        if cont == "YES":
                              print("The program will not be terminated")
                              print("Thank you for using the program")
                              break

                        elif cont == "NO":
                              print("The program will now continue")
                              continue

                        else:
                              print("Wrong Input. Invalid Answer")


                  elif num < 0:
                        print("Wrong Input. Must Be A Positive Number.")
                        continue

                  else:
                        print("Wrong Input. Invalid Answer")
                        continue

      except ValueError:
            print("Wrong Input. Must Be A Number.")
      
act22()


def chl1():
      print("\t\t\t\t\t\t\t\t\t\t\t    *\n\t\t\t\t\t\t\t\t\t\t\t  * * * \n\t\t\t\t\t\t\t\t\t\t\t* * * * * \n\t\t\t\t\t\t\t\t\t\t      * * * * * * * \n\t\t\t\t\t\t\t\t\t\t\t* * * * * \n\t\t\t\t\t\t\t\t\t\t\t  * * * \n\t\t\t\t\t\t\t\t\t\t\t    *")
