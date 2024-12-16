name = input(" please enter your name:  ")
isstudent = input(" are you a student of DLL:  ")

if isstudent.lower() == "yes":
	yearlevel = input("what year are you currently enrolled?",
	 "\nf- freshman \ns- sophomore \nr- senior:",
	  "\n please enter your grade level:  ")
	 
	if yearlevel.lower() == "f":
		print(f" hi {name}, freshman, welcome to DLL")
	
	elif  yearlevel.lower() == "s":
		print(f" hi {name}, senior, welcome to DLL")
else:
	print("thank you for using the system")
	
 