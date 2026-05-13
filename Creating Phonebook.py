# Creating a Phonebook with Dictionary features

PhoneDirectory = {}

print("Welcome to Phonebook!")

while True:

 print("1. Add a new Contact \n2. Search for a Contact \n3. Delete a contact \n4. List All Contacts \n5. Quit")

 option = int(input("Please choose from one of the options above: "))

 if option == 5:
  break
 
 elif option == 1:
  x = input("Please enter the name of person you want to enter in this phonebook: ")
  y = input("Please enter the person's phone number as well: ")
  PhoneDirectory.update({x:y})
  print(PhoneDirectory)

 elif option == 2:
  x = input("Please enter the name of person you are looking for: ")

  if x in PhoneDirectory:
   print("Phone Number: ",PhoneDirectory.setdefault(x))
  else:
   print("No Such Contact Exists!")

 elif option == 3:
   x = input("Please enter the name of person you are looking to delete: ")
   PhoneDirectory.pop(x)
   print(PhoneDirectory)

 elif option ==4:
  for x,y in PhoneDirectory.items():
   print(x,y)

 else:
  print("No such Option exists. Please try again.")   
