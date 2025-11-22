print(eval(input("ENTER")))
#----------------------- ASSIGNENT AGE ------------------#
user_age = int(input("enter age "))
if user_age >= 20:
     print("You are an adult.")
elif user_age > 13 and user_age < 19:
     print("You are a teenager")
elif user_age < 13:
     print("You are a child")
     #----------------------- ASSIMENT INCOME --------------------#
user_income = int(input("write you salary: "))
if user_income >= 100000:
     print("you have high income.")
elif user_income >= 50000:
     print("you have medium income.")
else:
     print("you have low income")

     #----------------------- ASSIGMENT TEMPERATURE -----------------------#
user_temperature = int(input("write temperature."))
if user_temperature >= 40:
     print("Its hot! Get some shade with you.")
elif user_temperature >25 and user_temperature < 45:
     print("Its moderate weather!")
elif user_temperature<25:
     print("its cold ")
else :
     print("i dont understand that.")

#----------------------- THE PASSWORD MANAGER -------------------------------# 
def user(username,password):
     if username.lower()  == "zulfi" and password == "1234":
          return "WELCOME ZULFI"
     else:
          return "Access is denied!!"
username = input("your name: ")
password = input("your password:  ")
message = user(username,password)
print(message)

#----------------------- PRACTICE  DATA FOR LOAN APPLICATION -------------------- #
user_name = input("Write your name:  ")
user_bank = input("Write your bank name:  ")

while True:
    #--------- CHECK YOUR CREDITS ----------- #


    user_input_credit = input("Write your credits:  ")  
    VALIDATION_LOAN_CREDIT = int(user_input_credit)
    USER_INPUT_CREDIT_2 = int(user_input_credit) >= VALIDATION_LOAN_CREDIT
    if USER_INPUT_CREDIT_2 != True:
         print("You dont have enough credits to acquire the loan")
         break
    else:
         print("You have enough credits to acquire the loan")
         break
    #------- THE APPLICATION FOR LOAN ---------- #


while True:
     user_input_loan = int(input("Write the Amount of loan you need "))
     if user_input_loan <= VALIDATION_LOAN_CREDIT:
         print(f"Your cannot have loan less than your credits which are {VALIDATION_LOAN_CREDIT}")
         break 
     #-------- THE APPLICATION CANCELED HERE -------- #
     
     #-------- IF THE LOAN IS GREATER THAN CREDITS THEN PROCEED FURTHER -------- #

     elif user_input_loan >= VALIDATION_LOAN_CREDIT:
         print(f"{user_name } you need loan of $ {user_input_loan}")  
         user_assure = input(f"{user_name } are you assure to acquire loan of ${user_input_loan} yes/no  ").upper()
     elif user_input_loan <= 0:
            print("Loan amount must be greater than zero")
            break
     if user_assure == "NO":
          print(f"MR. {user_name } you have cancelled the loan request ")  
     elif user_assure == "YES":
         print(f"MR. {user_name } you have successfully acquired the loan of $ {user_input_loan} has been transfered to your bank {user_bank} ")
         break
     else:
          print("You have cancelled the loan request")

#----------------------- CAR GAME SIMPLE ----------------------#
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
     #----------------------- CHANGE WEIGHT INTO POUNDs OR KILOs -------------------------#
user_weight= float(input("write your weight in either kilos or lbs : " )) #0.453592
change_into = input("You wanna change it in (L)lb or (K)kg : ").upper() #2.20462
if change_into == "L":
     converted = user_weight * 2.20 
     print(f"Your weight in   is {converted:.3f} pounds.")
elif change_into == "K":
     converted = user_weight * 0.45 
     print(f"Your weight  {converted:.3f} kilos.")
else:
     print("PLEASE WRITE (l) FOR POUNDS OR (k)) FOR KILOS!!!")

