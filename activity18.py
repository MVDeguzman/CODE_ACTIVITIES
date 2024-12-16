nt= eval(input("enter a number--->"))
for x in range (1,5):
    for r in range(1, nt + 1):
        for y in range(1, x +1):
            print("*", end= " ")
        for z in range(5, x, -1):
            print(" ", end= " ")
        print(end = " ")
    print()
