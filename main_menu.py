 try:
            compile = True

            while compile:

                  print("\n\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
                        "\n\tPrint statements - [1]"
                        "\n\tVariables        - [2]"
                        "\n\tOperators        - [3]"
                        "\n\tConditionals     - [4]"
                        "\n\tLoops            - [5]"
                        "\n\tList             - [6]"
                        "\n\tFunctions        - [7]"
                

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

                  
                  elif num == 0:
                        con = input("Do you want to continue? [Yes] / [No]: ").upper().strip()

                        if con == "YES":
                              print("The program will not be terminated")
                              print("Thank you for using the program")
                              break

                        elif con == "NO":
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