from bank import Bank

ans = True
while ans:
    print("*"*40)
    print("1. Get all customers")
    print("2. Add customer")
    print("3. Get customer by ssn")
    print("4. Change customer name")
    print("5. Delete customer")
    print("6. Add account")
    print("7. Get account")
    print("8. Deposit cash")
    print("9. Withdraw cash")
    print("10. Close account")
    print("*"*40)
    
    ans = input("Please make a choice from 1-10.: " )
    if ans == "1":
      
        Bank.get_customers()
