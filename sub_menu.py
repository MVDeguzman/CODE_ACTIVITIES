try:
            compile = True

            while compile:

                  print("\n\tSELECT FROM THE FOLLOWING ACTIVITY BELOW \n\t"
                        "\n\tActivity1 - [1]"
                        "\n\tActivity2 - [2]"
                        "\n\tActivity3 - [3]"
                        )
                

                  num = int(input("\n\n\tSelect Activity: "))

                  if num == 1:
                        act1()
                        continue

                  elif num == 2:
                        act2()
                        continue

                  elif num == 3:
                        act3()
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