expenseList = []
print("Welcome To Expense Tracker")

while True:
    print("===Menu===")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View All Amount")
    print("4. Exit")

    choice = int(input("Enter Your Choice Number"))

    if(choice==1):
        date = input("Enter Date")
        category = input("Enter Category")
        amount = float(input("Enter Amount Number"))
        description = input("Enter unique Description")

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }

        expenseList.append(expense)

        print("\n Added Successfully")

    elif(choice==2):
        if(len(expenseList)==0):
                print("No Expense List")
        else:
             print("Your Expense List")
             count = 1
             for eachexpense in expenseList:
                  print(f"Karcha Number {count}; {eachexpense['date']}; {eachexpense['category']}; {eachexpense['amount']}; {eachexpense['description']}")
                  count = count + 1

    elif(choice==3):
         total = 0
         for eachtotal in expenseList:
              total = total + {eachtotal['amount']}
            

         print(f"Total Amount = {amount}") 

    elif(choice==4):
        print("Apka Dhanyawaad")
        break

    else:
        print("Invalid Choice Number: Try Again")
     






