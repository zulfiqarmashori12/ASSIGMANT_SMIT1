
print("TYPE 00 AS FIRST NUMBER TO EXIT.")
while True:
     user_input_1 = float(input("WRITE FIRST NUMBER : "))
     if user_input_1 == 00: #------------ EXITING CALCULATER ----------------- #
          print("CALCULATER CLOSED!")
          break
     op = input("WRITE THE OPERATION TO PERFORM : ")
     user_input_2 = float(input("WRITE SECOND NUMBER : "))

     if op == "+":
          print(user_input_1+user_input_2)
     elif op == "-":
          print(user_input_1-user_input_2)
     elif op == "*":
          print(user_input_1*user_input_2)
     elif op == "/":
          print(user_input_1/user_input_2)
     elif op == "%":
          print(user_input_1/100*user_input_2)
     else:
          print("SYNTAX ERROR!!!!")
#--------------------------- START THE GAME ---------------------#
user_input = ""
started = False
user_input = input("TO OPEN GAME TYPE OPEN")
print("Start : To start the car  \nStop : To stop the car  \nQuit : To exit the game ")
while user_input.lower() == "open":
     user_command  = input().lower()
     if user_command == "start":
          if started:
               print("CAR IS ALREADY STARTED!!!!!!")
          else:
               started = True
               print("CAR STARTED !!!! lets goooo...")
               
          
     elif user_command == "stop":
          if not started:
               print("CAR IS ALREADY STOPPED!!!")
          else:
               started = False
               print("CAR STOPPED!!!!")
     elif user_command == "quit":
          print("YOU QUITED THE GAME!!!!!!!!")
          break
else:
     print("I DONT UNDERSTAND THAT!!!!!!!!")
user_name = input("Write your name:  ")
user_bank = input("Write your bank name:  ")
while True:
    #CHECK YOUR CREDITS


    user_input_credit = input("Write your credits:  ")  
    VALIDATION_LOAN_CREDIT = int(user_input_credit)
    USER_INPUT_CREDIT_2 = int(user_input_credit) >= VALIDATION_LOAN_CREDIT
    if USER_INPUT_CREDIT_2 != True:
         print("You dont have enough credits to acquire the loan")
         break
    else:
         print("You have enough credits to acquire the loan")
         break
    #THE APPLICATION FOR LOAN


while True:
     user_input_loan = int(input("Write the Amount of loan you need "))
     if user_input_loan <= VALIDATION_LOAN_CREDIT:
         print(f"Your cannot have loan less than your credits which are {VALIDATION_LOAN_CREDIT}")
         break 
     #THE APPLICATION CANCELED HERE
     #IF THE LOAN IS GREATER THAN CREDITS THEN PROCEED FURTHER

     elif user_input_loan >= VALIDATION_LOAN_CREDIT:
         print(f"{user_name } you need loan of $ {user_input_loan}")  
         user_assure = input(f"{user_name } are you assure to acquire loan of ${user_input_loan} yes/no  ").upper()
     elif user_input_loan <= 0:
            print("Loan amount must be greater than zero")
            break
     if user_assure == "NO":
          print(f"MR. {user_name } you have cancelled the loan request ")  
     elif user_assure == "YES":
         print(f"MR. {user_name } you have successfully  the loan of $ {user_input_loan} has been transfered to your bank {user_bank} ")
         break
     else:
          print("You have cancelled the loan request")


numbers = [ 5,2,5,2,2]
for x_count in numbers:
     output = ''
     for count in range(x_count):
          output += 'x'
     print(output)


     class1 ={"python","java","python","c","java","python","c","java","python","c","c++"}
print(f"we need {len(class1) } classes {tuple(class1)}")

dict1 = {
      'table':"a piece of furniture ",
      "cat":"a small animal",

}
user = input()
print(dict1.get(user))

sets = {1,2,"hello","world",9}
set2 = {3,2,1,7,9,0,"hello"}
print(sets.union(set2))
print(sets.intersection(set2))


while True: 
 user = int(input("WRITE A NUMBER: "))
 if  user <= 0:
      print(user," is negative number")
 elif   user > 0:
      print(user," is positive")
 elif user == 0:
      print("zero is neutral!")


user_name = str(input("WRITE YOUR NAME : "))
user_pass = int(input("write your password:"))
if user_name.lower() == "zulfiqar" and user_pass == 12345:
     print("Access granted") 
else:
     print("Acces denied")



age = int(input("enter age;"))
if age >= 18:
     print("YOU CAN VOTE!")
else:
     print("You are under age")